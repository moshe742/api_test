from enum import Enum
import typing
from datetime import datetime, timezone

import requests

from open_weather_api import config


class ForecastType(Enum):
    CURRENT = 1
    DAILY_16 = 2
    MULTIPLE = 3


class Units(Enum):
    STANDARD = 1
    METRIC = 2
    IMPERIAL = 3


def _update_day_times(forecast_data: typing.Dict, forecast: typing.Dict) -> None:
    sunrise = datetime.fromtimestamp(forecast_data['sys']['sunrise'], tz=timezone.utc)
    sunset = datetime.fromtimestamp(forecast_data['sys']['sunset'], tz=timezone.utc)
    forecast_time = datetime.fromtimestamp(forecast_data['dt'], tz=timezone.utc)

    forecast.update({
        'forecast_time': forecast_time,
        'sunrise_time': sunrise,
        'sunset_time': sunset
    })


def _get_main_data(forecast_data: typing.Dict) -> typing.Dict:
    return {
        'main': forecast_data['weather'][0]['main'],
        'description': forecast_data['weather'][0]['description'],
        'current_temp': forecast_data['main']['temp'],
        'min_temp': forecast_data['main']['temp_min'],
        'max_temp': forecast_data['main']['temp_max'],
        'feels_like': forecast_data['main']['feels_like'],
        'humidity': forecast_data['main']['humidity'],
        'pressure': forecast_data['main']['pressure'],
        'wind_speed': forecast_data['wind']['speed'],
        'wind_direction': forecast_data['wind']['deg'],
        'clouds': forecast_data['clouds']['all'],
        'city_name': forecast_data['name'],
        'country': forecast_data['sys']['country'],
    }


def _parse_forecast_current(forecast_data: typing.Dict) -> typing.Dict:
    forecast = _get_main_data(forecast_data)

    _update_day_times(forecast_data, forecast)

    if 'rain' in forecast_data:
        forecast['rain'] = forecast_data['rain']['1h']
    else:
        forecast['rain'] = 0

    if 'snow' in forecast_data:
        forecast['snow'] = forecast_data['snow']['1h']
    else:
        forecast['snow'] = 0

    return forecast


def _parse_forecast_daily(forecast_data: typing.Dict) -> typing.Dict:
    forecasts = []
    for forecast_day in forecast_data['list']:
        forecast_time = datetime.fromtimestamp(forecast_day['dt'], tz=timezone.utc)
        sunrise = datetime.fromtimestamp(forecast_day['sunrise'], tz=timezone.utc)
        sunset = datetime.fromtimestamp(forecast_day['sunset'], tz=timezone.utc)
        data = {
            'forecast_time': forecast_time,
            'sunrise_time': sunrise,
            'sunset_time': sunset,
            'day_temp': forecast_day['temp']['day'],
            'max_temp': forecast_day['temp']['max'],
            'min_temp': forecast_day['temp']['min'],
            'night_temp': forecast_day['temp']['night'],
            'eve_temp': forecast_day['temp']['eve'],
            'morning_temp': forecast_day['temp']['morn'],
            'day_feels_like': forecast_day['feels_like']['day'],
            'night_feels_like': forecast_day['feels_like']['night'],
            'eve_feels_like': forecast_day['feels_like']['eve'],
            'morning_feels_like': forecast_day['feels_like']['morn'],
            'pressure': forecast_day['pressure'],
            'humidity': forecast_day['humidity'],
            'main': forecast_day['weather'][0]['main'],
            'description': forecast_day['weather'][0]['description'],
            'wind_speed': forecast_day['speed'],
            'wind_direction': forecast_day['deg'],
            'precipitation_probability': forecast_day['pop']
        }

        if 'rain' in forecast_day:
            data['rain'] = forecast_day['rain']
        else:
            data['rain'] = 0

        if 'snow' in forecast_day:
            data['snow'] = forecast_day['snow']
        else:
            data['snow'] = 0

        forecasts.append(data)

    weather = {
        'city_name': forecast_data['city']['name'],
        'country': forecast_data['city']['country'],
        'forecasts': forecasts
    }

    return weather


def _parse_forecast_group(forecast_data: typing.Dict) -> typing.Dict:
    forecasts = {}
    for forecast_city in forecast_data['list']:
        forecast_time = datetime.fromtimestamp(forecast_city['dt'], timezone.utc)
        sunrise = datetime.fromtimestamp(forecast_city['sys']['sunrise'], timezone.utc)
        sunset = datetime.fromtimestamp(forecast_city['sys']['sunset'], timezone.utc)

        data = _get_main_data(forecast_city)
        data.update({
            'forecast_time': forecast_time,
            'sunrise_time': sunrise,
            'sunset_time': sunset
        })
        forecasts[forecast_city['name']] = data
    return forecasts


def get_city_forecast(city_id: typing.Union[int, typing.List],
                      forecast_type: ForecastType = ForecastType.CURRENT,
                      units: Units = Units.METRIC) -> typing.Dict:
    """get the weather of city_id city for forecast_type type"""
    api_parser = {
        ForecastType.CURRENT: {
            'api': 'weather',
            'parser': _parse_forecast_current,
        },
        ForecastType.DAILY_16: {
            'api': 'forecast/daily',
            'parser': _parse_forecast_daily,
        },
        ForecastType.MULTIPLE: {
            'api': 'group',
            'parser': _parse_forecast_group,
        }
    }

    if isinstance(city_id, list) and forecast_type == ForecastType.MULTIPLE:
        city_id = ','.join(str(c_id) for c_id in city_id)
    elif forecast_type == ForecastType.MULTIPLE:
        raise ValueError("if you choose Forecast.MULTIPLE you must give city_id as list of id's")
    elif isinstance(city_id, list):
        raise ValueError('if you choose a different option than Forecast.MULTIPLE you must give '
                         'city_id as int')

    payload = {
        'id': city_id,
        'appid': config.API_KEY,
        'units': units.name.lower()
    }

    url = f"{config.BASE_URL}{api_parser[forecast_type]['api']}"
    res = requests.get(url, params=payload)
    res = res.json()

    return api_parser[forecast_type]['parser'](res)
