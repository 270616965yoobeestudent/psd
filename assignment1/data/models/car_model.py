from peewee import CharField, AutoField, IntegerField, BooleanField
from .base_model import BaseModel


class CarModel(BaseModel):
    id = AutoField()
    make = CharField()
    model = CharField()
    year = CharField()
    mileage = IntegerField()
    available = BooleanField()
    minimum_day = IntegerField()
    maximum_day = IntegerField()
