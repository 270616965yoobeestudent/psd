from peewee import ForeignKeyField, AutoField, DateField, DateTimeField
from .user_model import UserModel
from .car_model import CarModel
from .base_model import BaseModel


class RentalModel(BaseModel):
    id = AutoField()
    user = ForeignKeyField(UserModel, backref="rentals")
    car = ForeignKeyField(CarModel)
    started_date = DateField()
    ended_date = DateField()
    created_at = DateTimeField()
