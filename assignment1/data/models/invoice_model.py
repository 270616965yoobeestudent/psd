from peewee import ForeignKeyField, AutoField, DateField, DateTimeField
from .base_model import BaseModel


class InvoiceModel(BaseModel):
    id = AutoField()
