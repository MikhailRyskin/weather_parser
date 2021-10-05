### Парсинг сайта с прогнозом погоды, занесение прогноза в БД, генерация открытки с погодой.
#### Описание.
Программа с консольным интерфейсом, получающая прогноз погоды путём парсинга сайта pogoda.mail.ru.
Добавление прогнозов за диапазон дат в базу данных и получение их из неё.
Выведение полученных прогнозов на консоль или формирование открытки с прогнозом и изображением,
соответствующим типу погоды(в качестве фона градиент цвета, отражающего тип погоды).  
(Подробная постановка задачи в модуле 01_weather.py).
#### Установка
Клонируйте репозиторий.  
**Внимание! Это учебный проект. Прогноз для Санкт-Петербурга. 
Для получения прогноза в конкретном месяце, необходимо в модуле parser_module.py
поменять месяц в FORECAST_SITE. Там-же можно поменять город**
```
FORECAST_SITE = 'https://pogoda.mail.ru/prognoz/sankt_peterburg/october-2021/'
```
Создайте и активируйте виртуальное окружение.
Установите зависимости в виртуальном окружении env/ :
```
pip install -r requirements.txt
```

#### Запуск
Находясь в папке проекта, запустите файл 01_weather.py
```
python 01_weather.py
```