import datetime
from models import WeatherBase


class DatabaseUpdater:
    def __init__(self, weather_dict):
        self.weather_dict = weather_dict

    def save_forecast(self, date_from, time_range):
        for day in range(time_range):
            if date_from in self.weather_dict:
                date = self.weather_dict[date_from][0]
                temperature = self.weather_dict[date_from][1]
                weather = self.weather_dict[date_from][2]
                WeatherBase.create(
                    date=date_from,
                    date_rus=date,
                    temperature=temperature,
                    weather=weather
                )
                one_day = datetime.timedelta(weeks=0, days=1)
                date_from += one_day
            else:
                return False
        return True

    def get_forecast(self, date_from, time_range):
        forecast_list = []
        for day in range(time_range):
            day_forecast = WeatherBase.get_or_none(WeatherBase.date == date_from)
            if day_forecast:
                forecast_list.append(day_forecast)
                one_day = datetime.timedelta(weeks=0, days=1)
                date_from += one_day
            else:
                return None
        return forecast_list
