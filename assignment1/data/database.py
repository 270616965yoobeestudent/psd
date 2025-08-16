import json
from peewee import SqliteDatabase

database = SqliteDatabase("app.db")


from .models.car_model import CarModel
from .models.user_model import UserModel


def _create_tables():
    with database:
        database.create_tables([UserModel, CarModel])


def _seed_data():
    if UserModel.select().count() == 0:
        with open("./data/seeds/users.json", "r") as f:
            cars = json.load(f)
            for car in cars:
                UserModel.create(**car)

    if CarModel.select().count() == 0:
        with open("./data/seeds/cars.json", "r") as f:
            cars = json.load(f)
            for car in cars:
                CarModel.create(**car)


def init_database():
    _create_tables()
    _seed_data()
