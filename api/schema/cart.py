from schema.base import BaseSchema

class CartBase(BaseSchema):
    user_id: int
    product_id: int
    total_qty: int = None
    price: int
    img: str
    gun_name: str
    gun_star: int

class Cart(CartBase):
    pass
class CartCreate(CartBase):
    user_id: int
    product_id: int
    total_qty: int
    price: int
    img: str
    gun_name: str
    gun_star: int