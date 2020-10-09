import os
from enum import Enum
import typing
from datetime import datetime, timezone

import requests

from . import config


class ForecastType(Enum):
    CURRENT = 1
    DAILY_16 = 2
    MULTIPLE = 3


class Units(Enum):
    STANDARD = 1
    METRIC = 2
    IMPERIAL = 3


def _parse_weather_current(weather_data: typing.Dict) -> typing.Dict:
    sunrise = datetime.fromtimestamp(weather_data['sys']['sunrise'], tz=timezone.utc)
    sunset = datetime.fromtimestamp(weather_data['sys']['sunset'], tz=timezone.utc)
    forecast_time = datetime.fromtimestamp(weather_data['dt'], tz=timezone.utc)

    weather = {
        'main': weather_data['weather'][0]['main'],
        'description': weather_data['weather'][0]['description'],
        'current_temp': weather_data['main']['temp'],
        'min_temp': weather_data['main']['temp_min'],
        'max_temp': weather_data['main']['temp_max'],
        'feels_like': weather_data['main']['feels_like'],
        'humidity': weather_data['main']['humidity'],
        'pressure': weather_data['main']['pressure'],
        'wind_speed': weather_data['wind']['speed'],
        'wind_direction': weather_data['wind']['deg'],
        'clouds': weather_data['clouds']['all'],
        'forecast_time': forecast_time,
        'sunrise_time': sunrise,
        'sunset_time': sunset,
        'city_name': weather_data['name'],
        'country': weather_data['sys']['country'],
    }

    if 'rain' in weather_data:
        weather['rain_1h'] = weather_data['rain']['1h']
        weather['rain_3h'] = weather_data['rain']['3h']

    if 'snow' in weather_data:
        weather['snow_1h'] = weather_data['snow']['1h']
        weather['snow_3h'] = weather_data['snow']['3h']

    return weather


def _parse_weather_daily(weather_data: typing.Dict) -> typing.Dict:
    forecasts = []
    for forecast in weather_data['list']:
        sunrise = datetime.fromtimestamp(forecast['sunrise'], tz=timezone.utc)
        sunset = datetime.fromtimestamp(forecast['sunset'], tz=timezone.utc)
        data = {
            'forecast_time': forecast['dt'],
            'sunrise_time': sunrise,
            'sunset_time': sunset,
            'day_temp': forecast['temp']['day'],
            'max_temp': forecast['temp']['max'],
            'min_temp': forecast['temp']['min'],
            'night_temp': forecast['temp']['night'],
            'eve_temp': forecast['temp']['eve'],
            'morning_temp': forecast['temp']['morn'],
            'day_feels_like': forecast['feels_like']['day'],
            'night_feels_like': forecast['feels_like']['night'],
            'eve_feels_like': forecast['feels_like']['eve'],
            'morning_feels_like': forecast['feels_like']['morn'],
            'pressure': forecast['pressure'],
            'humidity': forecast['humidity'],
            'main': forecast['weather'][0]['main'],
            'description': forecast['weather'][0]['description'],
            'wind_speed': forecast['speed'],
            'wind_direction': forecast['deg'],
            'precipitation_probability': forecast['pop']
        }

        if 'rain' in forecast:
            data['rain'] = forecast['rain'],

        if 'snow' in forecast:
            data['snow'] = forecast['snow']

        forecasts.append(data)

    weather = {
        'city_name': weather_data['city']['name'],
        'country': weather_data['country'],
        'forecasts': forecasts
    }

    return weather


def get_city_weather(city_id: typing.Union[int, typing.List], forecast_type: ForecastType = ForecastType.CURRENT,
                     units: Units = Units.METRIC) -> typing.Dict:
    """get the weather of city_id city for forecast_type type"""
    api_parser = {
        ForecastType.CURRENT: {
            'api': 'weather',
            'parser': _parse_weather_current,
        },
        ForecastType.DAILY_16: {
            'api': 'forecast/daily',
            'parser': _parse_weather_daily,
        },
        ForecastType.MULTIPLE: {
            'api': 'group',
            'parser': _parse_weather_current,
        }
    }

    if forecast_type == ForecastType.MULTIPLE and isinstance(city_id, list):
        city_id = ','.join(city_id)
    elif forecast_type == ForecastType.MULTIPLE:
        raise ValueError("if you choose Forecast.MULTIPLE you must give city_id as list of id's")

    payload = {
        'id': city_id,
        'appid': config.API_KEY,
        'units': units
    }

    res = requests.get(f"{config.BASE_URL}{api_parser[forecast_type]['api']}", params=payload)
    res = res.json()

    return api_parser[forecast_type]['parser'](res)
