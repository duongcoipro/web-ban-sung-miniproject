from model.base import BaseModel
from peewee import IntegerField, CharField

class Category(BaseModel):
    name = IntegerField()
    logo= CharField()
    class Meta:
        db_table='category'