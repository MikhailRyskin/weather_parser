import datetime
import re

from parser_module import MONTHS


def last_week():
    time_range = 7
    date_d = datetime.date.today() - datetime.timedelta(weeks=1, days=0)
    time_0 = datetime.time(hour=0, minute=0, second=0)
    date_dt = datetime.datetime.combine(date_d, time_0)
    return date_dt, time_range


def handle_date():
    while True:
        input_date = input('Введите дату в формате хх месяца хххх: ').lower()
        date_list = input_date.split(' ')
        re_date = re.compile(r'^(0[1-9]|[12][0-9]|3[01])[ ][а-я]{3,10}[ ](19|20)\d\d$')
        match = re.match(re_date, input_date)
        if match:
            month_rus = date_list[1]
            if month_rus in MONTHS:
                break
            else:
                print('Такого месяца не существует. Попробуйте ещё раз')
        else:
            print('Неверный формат даты. Попробуйте ещё раз.')
    range_choice = input('Прогноз на какой период: 1. 1 день. 2. 3 дня. 3. 5 дней:')
    if range_choice == '2':
        time_range = 3
    elif range_choice == '3':
        time_range = 5
    else:
        time_range = 1
    return input_date, time_range
