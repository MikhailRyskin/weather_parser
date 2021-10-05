import requests
from pprint import pprint
from bs4 import BeautifulSoup
import datetime

FORECAST_SITE = 'https://pogoda.mail.ru/prognoz/sankt_peterburg/october-2021/'

MONTHS = {'января': 'january', 'февраля': 'february', 'марта': 'march', 'апреля': 'april',
          'мая': 'may', 'июня': 'june', 'июля': 'july', 'августа': 'august',
          'сентября': 'september', 'октября': 'october', 'ноября': 'november', 'декабря': 'december'
          }


class WeatherMaker:
    def __init__(self):
        self.forecast_dict = {}

    def weather_parser(self):
        response = requests.get(FORECAST_SITE)
        if response.status_code == 200:
            html_doc = BeautifulSoup(response.text, features='html.parser')
            list_of_days = html_doc.find_all('div', 'day__date')
            list_of_temperatures = html_doc.find_all('div', 'day__temperature')
            list_of_weather = html_doc.find_all('div', 'day__description')

            for d, t, w in zip(list_of_days, list_of_temperatures, list_of_weather):
                day = d.text.lower()
                day_datetime, day_rus = self.date_conversion(day)
                temperature = t.text.split()[0][:-1]
                weather = w.text.strip().lower()
                self.forecast_dict[day_datetime] = [day_rus, temperature, weather]
        pprint(self.forecast_dict)

    def date_conversion(self, day):
        if day.startswith('с'):
            day = day[8:]
        day_rus = day
        for month_rus in MONTHS.keys():
            if day.find(month_rus) != -1:
                day = day.replace(month_rus, MONTHS[month_rus])
                break
        day_datetime = datetime.datetime.strptime(day, '%d %B %Y')
        return day_datetime, day_rus
