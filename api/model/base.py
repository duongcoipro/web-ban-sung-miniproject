import peewee
from operator import attrgetter

from sql_app.database import db

from peewee import CharField, IntegerField, Model,BooleanField

class BaseModel(Model):
    id= CharField()
    active= BooleanField()
    class Meta:
        database = db

    @classmethod
    def get_list(cls, get_dict=True, **kwargs):
        query = cls.handle_select()

        for key, value in kwargs.items():
            if value:
                query = query.where(attrgetter(key)(cls) == value)

        query = query
        if get_dict:
            query = query.dicts()

        query = query.order_by(cls.id)
        return list(query)

    @classmethod
    def handle_select(cls):
        return cls.select()

    @classmethod
    def soft_delete(cls, id):
        return cls.update(active=False).where(cls.id == id).execute()