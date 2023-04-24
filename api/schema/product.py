from schema.base import BaseSchema

class ProductBase(BaseSchema):
    name: str
    category: int
    cost: int
    star: int = 5
    img: str
    description: str
    sales: int
    qty: int
    price: int

class Product(ProductBase):
    id: int


class ProductCreate(ProductBase):
    name: str
    category: int
    cost: int
    star: int = 5 
    img: str
    description: str
    sales: int
    qty: int
    price: int