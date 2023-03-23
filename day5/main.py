from fastapi import FastAPI

from bson import ObjectId
from schematics.models import Model
from schematics.types import EmailType,StringType
import database
from pydantic import BaseModel
from typing import Dict, List, Any

class Input(BaseModel):
    name:str
    email:str

class User(Model):
    _id = ObjectId()
    name = StringType()
    email = EmailType()

newuser = User()

def create_user(name,email):
    _id = ObjectId()
    newuser.name = name
    newuser.email = email
    return dict(newuser)

app=FastAPI()

@app.post("/signup/")
def add_user(name: List | Dict | Any=None, email: List | Dict | Any=None):
    user = create_user(name,email)
    database.db.users.insert_one(user)
    return {"message":"User created successfully"}