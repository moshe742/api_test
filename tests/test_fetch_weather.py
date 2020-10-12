import datetime

import pytest
from pytest_mock import MockerFixture

from open_weather_api.fetch_weather import get_city_forecast, ForecastType


class OpenWeatherResponseRainy:
    def json(self):
        return {
            'coord': {
                'lon': -0.13,
                'lat': 51.51
            },
            'weather': [
                {
                    'id': 500,
                    'main': 'Rain',
                    'description': 'light rain',
                    'icon': '10d'
                }
            ],
            'base': 'stations',
            'main': {
                'temp': 11.14,
                'feels_like': 9.12,
                'temp_min': 10.56,
                'temp_max': 12,
                'pressure': 1015,
                'humidity': 87
            },
            'visibility': 10000,
            'wind': {
                'speed': 2.6,
                'deg': 170
            },
            'rain': {
                '1h': 0.47
            },
            'clouds': {
                'all': 100
            },
            'dt': 1602519816,
            'sys': {
                'type': 1,
                'id': 1414,
                'country': 'GB',
                'sunrise': 1602483586,
                'sunset': 1602522824
            },
            'timezone': 3600,
            'id': 2643743,
            'name': 'London',
            'cod': 200
        }


class OpenWeatherResponseSnow:
    def json(self):
        return {
            'coord': {
                'lon': -0.13,
                'lat': 51.51
            },
            'weather': [
                {
                    'id': 500,
                    'main': 'Rain',
                    'description': 'light rain',
                    'icon': '10d'
                }
            ],
            'base': 'stations',
            'main': {
                'temp': 11.14,
                'feels_like': 9.12,
                'temp_min': 10.56,
                'temp_max': 12,
                'pressure': 1015,
                'humidity': 87
            },
            'visibility': 10000,
            'wind': {
                'speed': 2.6,
                'deg': 170
            },
            'snow': {
                '1h': 0.47
            },
            'clouds': {
                'all': 100
            },
            'dt': 1602519816,
            'sys': {
                'type': 1,
                'id': 1414,
                'country': 'GB',
                'sunrise': 1602483586,
                'sunset': 1602522824
            },
            'timezone': 3600,
            'id': 2643743,
            'name': 'London',
            'cod': 200
        }


class OpenWeatherResponseDaily:
    def json(self):
        return {
            'city': {
                'id': 2643743,
                'name': 'London',
                'coord': {
                    'lon': -0.1257,
                    'lat': 51.5085
                },
                'country': 'GB',
                'population': 0,
                'timezone': 3600
            },
            'cod': '200',
            'message': 0.0562641,
            'cnt': 7,
            'list': [
                {
                    'dt': 1602500400,
                    'sunrise': 1602483585,
                    'sunset': 1602522823,
                    'temp': {
                        'day': 13.65,
                        'min': 9.27,
                        'max': 13.65,
                        'night': 11.06,
                        'eve': 11.01,
                        'morn': 9.27
                    },
                    'feels_like': {
                        'day': 9.7,
                        'night': 8.65,
                        'eve': 8.3,
                        'morn': 6.76
                    },
                    'pressure': 1019,
                    'humidity': 57,
                    'weather': [
                        {
                            'id': 501,
                            'main': 'Rain',
                            'description': 'moderate rain',
                            'icon': '10d'
                        }
                    ],
                    'speed': 4.12,
                    'deg': 217,
                    'clouds': 94,
                    'pop': 1,
                    'rain': 3.1,
                },
                {
                    'dt': 1602586800,
                    'sunrise': 1602570086,
                    'sunset': 1602609092,
                    'temp': {
                        'day': 11.95,
                        'min': 8.37,
                        'max': 11.96,
                        'night': 11.23,
                        'eve': 10.69,
                        'morn': 8.37
                    },
                    'feels_like': {
                        'day': 8.37,
                        'night': 6.52,
                        'eve': 6.04,
                        'morn': 5.01
                    },
                    'pressure': 1009,
                    'humidity': 58,
                    'weather': [
                        {
                            'id': 500,
                            'main': 'Rain',
                            'description': 'light rain',
                            'icon': '10d'
                        }
                    ],
                    'speed': 3.21,
                    'deg': 16,
                    'clouds': 96,
                    'pop': 0.98,
                    'rain': 2.36,
                },
                {
                    'dt': 1602673200,
                    'sunrise': 1602656588,
                    'sunset': 1602695363,
                    'temp': {
                        'day': 14.61,
                        'min': 10.66,
                        'max': 14.91,
                        'night': 11.11,
                        'eve': 12.64,
                        'morn': 10.66
                    },
                    'feels_like': {
                        'day': 10.11,
                        'night': 6.5,
                        'eve': 8.43,
                        'morn': 6.74
                    },
                    'pressure': 1021,
                    'humidity': 55,
                    'weather': [
                        {
                            'id': 500,
                            'main': 'Rain',
                            'description': 'light rain',
                            'icon': '10d'
                        }
                    ],
                    'speed': 5.02,
                    'deg': 44,
                    'clouds': 45,
                    'pop': 0.55,
                    'rain': 1.19,
                },
                {
                    'dt': 1602759600,
                    'sunrise': 1602743090,
                    'sunset': 1602781634,
                    'temp': {
                        'day': 12.58,
                        'min': 9.6,
                        'max': 12.95,
                        'night': 10.16,
                        'eve': 10.93,
                        'morn': 9.6
                    },
                    'feels_like': {
                        'day': 8.21,
                        'night': 6.91,
                        'eve': 6.94,
                        'morn': 5.24
                    },
                    'pressure': 1023,
                    'humidity': 59,
                    'weather': [
                        {
                            'id': 500,
                            'main': 'Rain',
                            'description': 'light rain',
                            'icon': '10d'
                        }
                    ],
                    'speed': 4.57,
                    'deg': 12,
                    'clouds': 55,
                    'pop': 0.3,
                    'rain': 0.25,
                },
                {
                    'dt': 1602846000,
                    'sunrise': 1602829592,
                    'sunset': 1602867906,
                    'temp': {
                        'day': 12.65,
                        'min': 8.33,
                        'max': 12.65,
                        'night': 10.03,
                        'eve': 11.13,
                        'morn': 8.33
                    },
                    'feels_like': {
                        'day': 8.99,
                        'night': 7.53,
                        'eve': 8.13,
                        'morn': 6.04
                    },
                    'pressure': 1021,
                    'humidity': 48,
                    'weather': [
                        {
                            'id': 802,
                            'main': 'Clouds',
                            'description': 'scattered clouds',
                            'icon': '03d'
                        }
                    ],
                    'speed': 2.82,
                    'deg': 102,
                    'clouds': 27,
                    'pop': 0,
                },
                {
                    'dt': 1602932400,
                    'sunrise': 1602916095,
                    'sunset': 1602954179,
                    'temp': {
                        'day': 11.94,
                        'min': 10.02,
                        'max': 12.81,
                        'night': 10.17,
                        'eve': 11.1,
                        'morn': 10.6
                    },
                    'feels_like': {
                        'day': 8.19,
                        'night': 6.32,
                        'eve': 7.55,
                        'morn': 7.2
                    },
                    'pressure': 1020,
                    'humidity': 63,
                    'weather': [
                        {
                            'id': 804,
                            'main': 'Clouds',
                            'description': 'overcast clouds',
                            'icon': '04d'
                        }
                    ],
                    'speed': 3.79,
                    'deg': 61,
                    'clouds': 100,
                    'pop': 0,
                },
                {
                    'dt': 1603018800,
                    'sunrise': 1603002598,
                    'sunset': 1603040452,
                    'temp': {
                        'day': 12.79,
                        'min': 9.07,
                        'max': 13.42,
                        'night': 11,
                        'eve': 11.42,
                        'morn': 9.07
                    },
                    'feels_like': {
                        'day': 9.04,
                        'night': 7.84,
                        'eve': 8.42,
                        'morn': 6.75
                    },
                    'pressure': 1013,
                    'humidity': 52,
                    'weather': [
                        {
                            'id': 803,
                            'main': 'Clouds',
                            'description': 'broken clouds',
                            'icon': '04d'
                        }
                    ],
                    'speed': 3.26,
                    'deg': 111,
                    'clouds': 74,
                    'pop': 0,
                    'snow': 0.3
                }
            ]
        }


class OpenWeatherResponseGroup:
    def json(self):
        return {
            'cnt': 2,
            'list': [
                {
                    'coord': {
                        'lon': -0.13,
                        'lat': 51.51
                    },
                    'sys': {
                        'country': 'GB',
                        'timezone': 3600,
                        'sunrise': 1602483586,
                        'sunset': 1602522824
                    },
                    'weather': [
                        {
                            'id': 500,
                            'main': 'Rain',
                            'description': 'light rain',
                            'icon': '10n'
                        }
                    ],
                    'main': {
                        'temp': 10.37,
                        'feels_like': 8.41,
                        'temp_min': 10,
                        'temp_max': 11.11,
                        'pressure': 1015,
                        'humidity': 93
                    },
                    'visibility': 8000,
                    'wind': {
                        'speed': 2.6,
                        'deg': 220
                    },
                    'clouds': {
                        'all': 75
                    },
                    'dt': 1602526276,
                    'id': 2643743,
                    'name': 'London'
                },
                {
                    'coord': {
                        'lon': -71.06,
                        'lat': 42.36
                    },
                    'sys': {
                        'country': 'US',
                        'timezone': -14400,
                        'sunrise': 1602500038,
                        'sunset': 1602540413
                    },
                    'weather': [
                        {
                            'id': 804,
                            'main': 'Clouds',
                            'description': 'overcast clouds',
                            'icon': '04d'
                        }
                    ],
                    'main': {
                        'temp': 12.15,
                        'feels_like': 4.95,
                        'temp_min': 11.11,
                        'temp_max': 12.78,
                        'pressure': 1027,
                        'humidity': 62
                    },
                    'visibility': 10000,
                    'wind': {
                        'speed': 8.7,
                        'deg': 70
                    },
                    'clouds': {
                        'all': 90
                    },
                    'dt': 1602526431,
                    'id': 4930956,
                    'name': 'Boston'
                }
            ]
        }


def test_fetch_forecast_current_rainy(mocker: MockerFixture) -> None:
    requests_mock = mocker.patch('requests.get')
    requests_mock.return_value = OpenWeatherResponseRainy()
    expected_result = {
        'main': 'Rain',
        'description': 'light rain',
        'current_temp': 11.14,
        'min_temp': 10.56,
        'max_temp': 12,
        'feels_like': 9.12,
        'humidity': 87,
        'pressure': 1015,
        'wind_speed': 2.6,
        'wind_direction': 170,
        'clouds': 100,
        'forecast_time': datetime.datetime(2020, 10, 12, 16, 23, 36, tzinfo=datetime.timezone.utc),
        'sunrise_time': datetime.datetime(2020, 10, 12, 6, 19, 46, tzinfo=datetime.timezone.utc),
        'sunset_time': datetime.datetime(2020, 10, 12, 17, 13, 44, tzinfo=datetime.timezone.utc),
        'city_name': 'London',
        'country': 'GB',
        'rain': 0.47,
        'snow': 0,
    }

    actual_result = get_city_forecast(2643743, ForecastType.CURRENT)
    assert expected_result == actual_result


def test_fetch_forecast_current_snowy(mocker: MockerFixture) -> None:
    requests_mock = mocker.patch('requests.get')
    requests_mock.return_value = OpenWeatherResponseSnow()
    expected_result = {
        'main': 'Rain',
        'description': 'light rain',
        'current_temp': 11.14,
        'min_temp': 10.56,
        'max_temp': 12,
        'feels_like': 9.12,
        'humidity': 87,
        'pressure': 1015,
        'wind_speed': 2.6,
        'wind_direction': 170,
        'clouds': 100,
        'forecast_time': datetime.datetime(2020, 10, 12, 16, 23, 36, tzinfo=datetime.timezone.utc),
        'sunrise_time': datetime.datetime(2020, 10, 12, 6, 19, 46, tzinfo=datetime.timezone.utc),
        'sunset_time': datetime.datetime(2020, 10, 12, 17, 13, 44, tzinfo=datetime.timezone.utc),
        'city_name': 'London',
        'country': 'GB',
        'rain': 0,
        'snow': 0.47,
    }

    actual_result = get_city_forecast(2643743, ForecastType.CURRENT)
    assert expected_result == actual_result


def test_fetch_forecast_daily(mocker: MockerFixture) -> None:
    requests_mock = mocker.patch('requests.get')
    requests_mock.return_value = OpenWeatherResponseDaily()
    expected_result = {
        'city_name': 'London',
        'country': 'GB',
        'forecasts': [
            {
                'forecast_time': datetime.datetime(2020, 10, 12, 11, 0, tzinfo=datetime.timezone.utc),
                'sunrise_time': datetime.datetime(2020, 10, 12, 6, 19, 45, tzinfo=datetime.timezone.utc),
                'sunset_time': datetime.datetime(2020, 10, 12, 17, 13, 43, tzinfo=datetime.timezone.utc),
                'day_temp': 13.65,
                'max_temp': 13.65,
                'min_temp': 9.27,
                'night_temp': 11.06,
                'eve_temp': 11.01,
                'morning_temp': 9.27,
                'day_feels_like': 9.7,
                'night_feels_like': 8.65,
                'eve_feels_like': 8.3,
                'morning_feels_like': 6.76,
                'pressure': 1019,
                'humidity': 57,
                'main': 'Rain',
                'description': 'moderate rain',
                'wind_speed': 4.12,
                'wind_direction': 217,
                'precipitation_probability': 1,
                'rain': 3.1,
                'snow': 0,
            },
            {
                'forecast_time': datetime.datetime(2020, 10, 13, 11, 0, tzinfo=datetime.timezone.utc),
                'sunrise_time': datetime.datetime(2020, 10, 13, 6, 21, 26, tzinfo=datetime.timezone.utc),
                'sunset_time': datetime.datetime(2020, 10, 13, 17, 11, 32, tzinfo=datetime.timezone.utc),
                'day_temp': 11.95,
                'max_temp': 11.96,
                'min_temp': 8.37,
                'night_temp': 11.23,
                'eve_temp': 10.69,
                'morning_temp': 8.37,
                'day_feels_like': 8.37,
                'night_feels_like': 6.52,
                'eve_feels_like': 6.04,
                'morning_feels_like': 5.01,
                'pressure': 1009,
                'humidity': 58,
                'main': 'Rain',
                'description': 'light rain',
                'wind_speed': 3.21,
                'wind_direction': 16,
                'precipitation_probability': 0.98,
                'rain': 2.36,
                'snow': 0
            },
            {
                'forecast_time': datetime.datetime(2020, 10, 14, 11, 0, tzinfo=datetime.timezone.utc),
                'sunrise_time': datetime.datetime(2020, 10, 14, 6, 23, 8, tzinfo=datetime.timezone.utc),
                'sunset_time': datetime.datetime(2020, 10, 14, 17, 9, 23, tzinfo=datetime.timezone.utc),
                'day_temp': 14.61,
                'max_temp': 14.91,
                'min_temp': 10.66,
                'night_temp': 11.11,
                'eve_temp': 12.64,
                'morning_temp': 10.66,
                'day_feels_like': 10.11,
                'night_feels_like': 6.5,
                'eve_feels_like': 8.43,
                'morning_feels_like': 6.74,
                'pressure': 1021,
                'humidity': 55,
                'main': 'Rain',
                'description': 'light rain',
                'wind_speed': 5.02,
                'wind_direction': 44,
                'precipitation_probability': 0.55,
                'rain': 1.19,
                'snow': 0
            },
            {
                'forecast_time': datetime.datetime(2020, 10, 15, 11, 0, tzinfo=datetime.timezone.utc),
                'sunrise_time': datetime.datetime(2020, 10, 15, 6, 24, 50, tzinfo=datetime.timezone.utc),
                'sunset_time': datetime.datetime(2020, 10, 15, 17, 7, 14, tzinfo=datetime.timezone.utc),
                'day_temp': 12.58,
                'max_temp': 12.95,
                'min_temp': 9.6,
                'night_temp': 10.16,
                'eve_temp': 10.93,
                'morning_temp': 9.6,
                'day_feels_like': 8.21,
                'night_feels_like': 6.91,
                'eve_feels_like': 6.94,
                'morning_feels_like': 5.24,
                'pressure': 1023,
                'humidity': 59,
                'main': 'Rain',
                'description': 'light rain',
                'wind_speed': 4.57,
                'wind_direction': 12,
                'precipitation_probability': 0.3,
                'rain': 0.25,
                'snow': 0
            },
            {
                'forecast_time': datetime.datetime(2020, 10, 16, 11, 0, tzinfo=datetime.timezone.utc),
                'sunrise_time': datetime.datetime(2020, 10, 16, 6, 26, 32, tzinfo=datetime.timezone.utc),
                'sunset_time': datetime.datetime(2020, 10, 16, 17, 5, 6, tzinfo=datetime.timezone.utc),
                'day_temp': 12.65,
                'max_temp': 12.65,
                'min_temp': 8.33,
                'night_temp': 10.03,
                'eve_temp': 11.13,
                'morning_temp': 8.33,
                'day_feels_like': 8.99,
                'night_feels_like': 7.53,
                'eve_feels_like': 8.13,
                'morning_feels_like': 6.04,
                'pressure': 1021,
                'humidity': 48,
                'main': 'Clouds',
                'description': 'scattered clouds',
                'wind_speed': 2.82,
                'wind_direction': 102,
                'precipitation_probability': 0,
                'rain': 0,
                'snow': 0
            },
            {
                'forecast_time': datetime.datetime(2020, 10, 17, 11, 0, tzinfo=datetime.timezone.utc),
                'sunrise_time': datetime.datetime(2020, 10, 17, 6, 28, 15, tzinfo=datetime.timezone.utc),
                'sunset_time': datetime.datetime(2020, 10, 17, 17, 2, 59, tzinfo=datetime.timezone.utc),
                'day_temp': 11.94,
                'max_temp': 12.81,
                'min_temp': 10.02,
                'night_temp': 10.17,
                'eve_temp': 11.1,
                'morning_temp': 10.6,
                'day_feels_like': 8.19,
                'night_feels_like': 6.32,
                'eve_feels_like': 7.55,
                'morning_feels_like': 7.2,
                'pressure': 1020,
                'humidity': 63,
                'main': 'Clouds',
                'description': 'overcast clouds',
                'wind_speed': 3.79,
                'wind_direction': 61,
                'precipitation_probability': 0,
                'rain': 0,
                'snow': 0
            },
            {
                'forecast_time': datetime.datetime(2020, 10, 18, 11, 0, tzinfo=datetime.timezone.utc),
                'sunrise_time': datetime.datetime(2020, 10, 18, 6, 29, 58, tzinfo=datetime.timezone.utc),
                'sunset_time': datetime.datetime(2020, 10, 18, 17, 0, 52, tzinfo=datetime.timezone.utc),
                'day_temp': 12.79,
                'max_temp': 13.42,
                'min_temp': 9.07,
                'night_temp': 11,
                'eve_temp': 11.42,
                'morning_temp': 9.07,
                'day_feels_like': 9.04,
                'night_feels_like': 7.84,
                'eve_feels_like': 8.42,
                'morning_feels_like': 6.75,
                'pressure': 1013,
                'humidity': 52,
                'main': 'Clouds',
                'description': 'broken clouds',
                'wind_speed': 3.26,
                'wind_direction': 111,
                'precipitation_probability': 0,
                'rain': 0,
                'snow': 0.3,
            }
        ]
    }
    actual_result = get_city_forecast(2643743, ForecastType.DAILY_16)
    assert expected_result == actual_result


def test_fetch_forecast_group(mocker: MockerFixture) -> None:
    requests_mock = mocker.patch('requests.get')
    requests_mock.return_value = OpenWeatherResponseGroup()
    expected_result = {
        'London': {
            'main': 'Rain',
            'description': 'light rain',
            'current_temp': 10.37,
            'min_temp': 10,
            'max_temp': 11.11,
            'feels_like': 8.41,
            'humidity': 93,
            'pressure': 1015,
            'wind_speed': 2.6,
            'wind_direction': 220,
            'clouds': 75,
            'city_name': 'London',
            'country': 'GB',
            'forecast_time': datetime.datetime(2020, 10, 12, 18, 11, 16, tzinfo=datetime.timezone.utc),
            'sunrise_time': datetime.datetime(2020, 10, 12, 6, 19, 46, tzinfo=datetime.timezone.utc),
            'sunset_time': datetime.datetime(2020, 10, 12, 17, 13, 44, tzinfo=datetime.timezone.utc)
        },
        'Boston': {
            'main': 'Clouds',
            'description': 'overcast clouds',
            'current_temp': 12.15,
            'min_temp': 11.11,
            'max_temp': 12.78,
            'feels_like': 4.95,
            'humidity': 62,
            'pressure': 1027,
            'wind_speed': 8.7,
            'wind_direction': 70,
            'clouds': 90,
            'city_name': 'Boston',
            'country': 'US',
            'forecast_time': datetime.datetime(2020, 10, 12, 18, 13, 51, tzinfo=datetime.timezone.utc),
            'sunrise_time': datetime.datetime(2020, 10, 12, 10, 53, 58, tzinfo=datetime.timezone.utc),
            'sunset_time': datetime.datetime(2020, 10, 12, 22, 6, 53, tzinfo=datetime.timezone.utc)
        }
    }
    actual_result = get_city_forecast([2643743, 4930956], ForecastType.MULTIPLE)
    assert expected_result == actual_result


def test_fetch_forecast_group_fail_multiple_no_list() -> None:
    with pytest.raises(ValueError):
        get_city_forecast(2643743, ForecastType.MULTIPLE)


def test_fetch_forecast_group_fail_single_list() -> None:
    with pytest.raises(ValueError):
        get_city_forecast([2643743], ForecastType.CURRENT)
