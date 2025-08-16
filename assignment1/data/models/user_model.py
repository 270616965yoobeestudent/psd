from peewee import CharField
from .base_model import BaseModel


class UserModel(BaseModel):
    username = CharField(unique=True, primary_key=True)
    password = CharField()
    role = CharField()