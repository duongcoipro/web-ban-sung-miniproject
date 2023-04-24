from fastapi import APIRouter
from model.user import User as UserModel
from schema.user import User, UserCreate, UserLogin
from typing import List
from playhouse.shortcuts import model_to_dict

router = APIRouter()


@router.get('/', response_model=List[User])
def get_user():
    return UserModel.get_list()


@router.post('/', response_model=User)
def create_user(user: UserCreate):
    return UserModel.create(**user.dict())


@router.post('/login')
def login(user: UserLogin):
    user = UserModel.get_or_none(user_name=user.user_name, user_password=user.user_password)  # noqa: E501
    if not user:
        return {
            'status': 400, 'data': None
        }

    user = model_to_dict(user)
    user.pop('password', None)
    return {
        'status': 200, 'data': user
    }
