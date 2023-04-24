from fastapi import FastAPI, Depends, APIRouter
from model.category import Category 
from schema import category as schema
from schema.category import Category as CategorySchema
from sql_app.database import db,db_state_default
from typing import List
from router import api
from fastapi.middleware.cors import CORSMiddleware


db.connect()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event('startup')
def startup():
    if db.is_closed():
        db.connect()

@app.on_event('shutdown')
def shutdown():
    if not db.is_closed():
        db.close()

app.include_router(api.router)