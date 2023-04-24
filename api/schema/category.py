from schema.base import BaseSchema

class Category(BaseSchema):
    name: str
    active: bool
    logo: str =None

class CategoryCreate(BaseSchema):
    name: str
    active: bool
    logo: str =None