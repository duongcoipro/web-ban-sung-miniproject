from contextvars import ContextVar
import peewee
import psycopg2
from peewee import *


db_state_default = {"closed": None, "conn": None,
                    "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]

db = peewee.PostgresqlDatabase('default', user="postgres", password="postgres", host="db", port=5432)  # noqa: E501
