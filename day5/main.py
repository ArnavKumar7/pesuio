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

@app.post("/signup")
def add_user(name: List | Dict | Any=None, email: List | Dict | Any=None):
    user = create_user(name,email)
    database.db.users.insert_one(user)
    return {"message":"User created successfully"}
@app.get("/users")
def get_users():
    l=[]
    users = database.db.users.find()
    for i in users:
        i['_id']=str(i['_id'])
        l.append(i)
    return l

@app.get('/users/{name}')
def get_user(name: str):
    user = database.db.users.find_one({"name":name})
    user['_id']=str(user['_id'])
    return user

@app.put("/updateuser")
def update_user(name: List | Dict | Any=None, email: List | Dict | Any=None):
    database.db.users.update_one({"name":name},{"$set":{"email":email}})
    return {"message":"User updated successfully"}

@app.delete("/deleteuser/{name}")
def delete_user(name: str):
    database.db.users.delete_one({"name":name})
    return {"message":"User deleted successfully"}