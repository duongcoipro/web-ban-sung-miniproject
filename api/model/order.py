from operator import attrgetter
from model.base import BaseModel
from peewee import IntegerField, CharField, TimeField


class Order(BaseModel):
    user_id= IntegerField()
    product_id= IntegerField()
    total_qty= IntegerField()
    status= CharField()
    total_price = IntegerField()
    address= CharField()
    phone= IntegerField()
    gun_name= CharField()
    gun_id= IntegerField()
    gun_qty= IntegerField()
    created_at= CharField()
    user_name= CharField()
    
    class Meta:
        db_table='order'
    
    @classmethod
    def get_listfull(cls):
        return list(cls.select())
    
    def get_list(cls, get_dict=True, **kwargs):
        query = cls.handle_select()

        for key, value in kwargs.items():
            if value:
                query = query.where(attrgetter(key)(cls) == value)

        query = query.where(cls.active)
        if get_dict:
            query = query.dicts()

        query = query.order_by(cls.user_id)
        return list(query)

