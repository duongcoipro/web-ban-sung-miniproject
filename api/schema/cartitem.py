from schema.base import BaseSchema

class Cart_itemBase(BaseSchema):
    cart_id: int
    gun_id: int
    gun_qty: int
    price: int
    img: str
    gun_type: str

class Cart(Cart_itemBase):
    pass

class Cart_itemCreate(Cart_itemBase):
    cart_id: int
    gun_id: int
    gun_qty: int
    price: int
    img: str
    gun_type: str

class Cartitemcount(Cart_itemBase):
    pass 