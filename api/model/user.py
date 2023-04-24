from peewee import CharField, IntegerField
from model.base import BaseModel


class User(BaseModel):
    user_name= CharField()
    tel = CharField()
    email = CharField()
    address = CharField()
    user_type = IntegerField()
    user_password = CharField()

