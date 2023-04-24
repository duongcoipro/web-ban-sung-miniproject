from fastapi import APIRouter
from model.order import Order as OrderModel
from schema.order import Order, OrderCreate,Orderone
from typing import List
from playhouse.shortcuts import model_to_dict

router = APIRouter()

@router.get('/full', response_model=List[Order])
def get_order():
    return OrderModel.get_listfull()


@router.post('/', response_model=Order)
def create_order(cart: OrderCreate):
    return OrderModel.create(**cart.dict())

@router.get('/one/{user_id}')
def get_oneorder(user_id: str):
    query = OrderModel.select().where(OrderModel.user_id == user_id)
    orders = [model_to_dict(order) for order in query]

    if not orders:
        return {
             None
        }
    return orders