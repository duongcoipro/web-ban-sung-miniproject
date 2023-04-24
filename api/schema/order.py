from schema.base import BaseSchema

class OrderBase(BaseSchema):
    user_id: int
    product_id: int
    total_qty: int
    status: str
    total_price : int
    address: str
    phone: int
    gun_name: str
    gun_id: int
    gun_qty: int
    created_at: str
    active: bool
    user_name: str

class Order(OrderBase):
    pass

class Orderone(BaseSchema):
     user_id: int

class OrderCreate(OrderBase):
    user_id: int
    product_id: int
    total_qty: int
    status: str
    gun_qty: int
    total_price : int
    address: str
    phone: int
    gun_name: str
    gun_id: int
    active: bool
    created_at: str
    user_name: str
