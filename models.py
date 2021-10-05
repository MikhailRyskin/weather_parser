import peewee
from playhouse.db_url import connect

# database = peewee.SqliteDatabase('weather_forecast.db')

database_proxy = peewee.DatabaseProxy()  # Create a proxy for our db.


class BaseTable(peewee.Model):
    class Meta:
        # database = database
        database = database_proxy


url = 'sqlite:///weather_forecast.db'
database = connect(url)
database_proxy.initialize(database)


class WeatherBase(BaseTable):
    date = peewee.DateTimeField()
    date_rus = peewee.CharField()
    temperature = peewee.CharField()
    weather = peewee.CharField()


database.create_tables([WeatherBase, ])
