from fastapi import APIRouter
from model.cart import Cart as CartModel
from schema.cart import Cart, CartCreate
from typing import List
from playhouse.shortcuts import model_to_dict
from peewee import SQL, fn

router = APIRouter()

@router.get('/', response_model=List[Cart])
def get_cart():
    return CartModel.get_list()

@router.get('/forcheckout', response_model=List[Cart])
def get_total(user_id: int):
    query = CartModel.select(CartModel.id, CartModel.user_id, CartModel.product_id, CartModel.gun_name, fn.Sum(CartModel.price).alias('price'),  # noqa: E501
        fn.Sum(CartModel.total_qty).alias('total_qty'), CartModel.img, CartModel.gun_star)\
        .where(CartModel.user_id == user_id)\
        .group_by(CartModel.user_id, CartModel.product_id, CartModel.gun_name, CartModel.id, CartModel.img, CartModel.gun_star) # noqa: E501
    return list(query)

@router.get('/one')
def get_onecart(user_id: str):
    query = CartModel.select().where(CartModel.user_id == user_id)
    carts = [model_to_dict(cart) for cart in query]

    if not carts:
        return {
             None
        }
    return carts

@router.post('/', response_model=Cart)
def create_cart(cart: CartCreate):
    return CartModel.create(**cart.dict())

@router.delete('/{product_id}')
def delete_cart(user_id: int, product_id: int):
    query = CartModel.delete().where((CartModel.user_id == user_id) & (CartModel.product_id == product_id))  # noqa: E501
    query.execute()
    return {'message': f'Deleted cart item with user_id={user_id} and product_id={product_id}'}# noqa: E501

@router.delete('/{product_id}')
def delete_cart(user_id: int, product_id: int):
    query = CartModel.delete().where((CartModel.user_id == user_id) & (CartModel.product_id == product_id)).LIMIT(1) # noqa: E501
    deleted_rows = query.execute()
    if deleted_rows:
        return {'message': f'Deleted cart item with user_id={user_id} and product_id={product_id}'} # noqa: E501
    else:
        return {'message': f'Cart item with user_id={user_id} and product_id={product_id} not found'} # noqa: E501