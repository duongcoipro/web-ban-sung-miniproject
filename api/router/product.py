from fastapi import APIRouter
from fastapi import APIRouter, HTTPException
from model.product import Product
from schema import product as schema
from typing import List
from playhouse.shortcuts import model_to_dict

router= APIRouter()


@router.get('/', response_model=List[schema.Product])
def get_product():
    return  Product.get_list()

@router.post('/',response_model=schema.Product)
def create_product(product: schema.ProductCreate):
    return  Product.create(**product.dict())

@router.delete('/{id}')
def delete_product(id: int):
    #product = model_to_dict(Product.get_by_id(id)),
    print(id),
    Product.delete_by_id(id)

@router.get('/get_one/{id}')
def get_one(id: int):
    product = Product.get_or_none(id=id)
    if not product:
        return {
            'data': 'Not Found'
        }
    product = model_to_dict(product)
    return product