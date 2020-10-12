from open_weather_api.fetch_weather import (
    ForecastType,
    get_city_forecast,
    Units,
)


def main():
    res = get_city_forecast([2643743, 4930956], ForecastType.MULTIPLE)
    print(res)


if __name__ == '__main__':
    main()
