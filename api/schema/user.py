from schema.base import BaseSchema


class UserBase(BaseSchema):
    user_name: str
    tel: str
    email: str
    user_type: int


class User(UserBase):
    id: int


class UserCreate(UserBase):
    user_password: str


class UserUpdate(UserBase):
    pass


class UserLogin(BaseSchema):
    user_name: str
    user_password: str

