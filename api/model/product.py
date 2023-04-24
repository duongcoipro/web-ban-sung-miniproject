from model.base import BaseModel
from peewee import IntegerField, CharField, ForeignKeyField, BooleanField

class Product(BaseModel):
    # ForeignKeyField(Category,column_name='category')
    name = CharField()
    cost= IntegerField()
    price= IntegerField()
    star= IntegerField()
    img = CharField()
    description= CharField()
    sales= IntegerField()
    category= IntegerField()
    qty= IntegerField()

    class Meta:
        db_table='product'

    @classmethod
    def get_list(cls):
        return list(cls.select())
    
    def get_list1(cls, limit=None, **kwargs):
        query = (
            Product.select().where(Product.id == limit).get().dict()
        )

        return list(query)