from model.base import BaseModel
from peewee import IntegerField, CharField, ForeignKeyField, BooleanField

class Cart_item(BaseModel):
    cart_id= IntegerField()
    gun_id= IntegerField()
    gun_qty= IntegerField()
    price = IntegerField()
    img= CharField()
    gun_type= CharField()

    class Meta:
        db_table='cart_item'
    
    @classmethod
    def get_list(cls):
        return list(cls.select())


