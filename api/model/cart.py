from model.base import BaseModel
from peewee import IntegerField, CharField, ForeignKeyField, BooleanField, SQL


class Cart(BaseModel):
    user_id= IntegerField()
    product_id= IntegerField()
    total_qty= IntegerField()
    price = IntegerField()
    img= CharField()
    gun_name= CharField()
    gun_star= IntegerField()
    
    class Meta:
        db_table='cart'
    
    @classmethod
    def get_list(cls):
        return list(cls.select())


