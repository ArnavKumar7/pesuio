from fastapi import FastAPI

from enum import Enum

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class ModelName(str, Enum):
    pesuio = "day3"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def item(item_id):
    return {"item_id": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.pesuio:
        return {"model_name": model_name, "message": "Web Dev"}

    return {"model_name": model_name, "message": "residuals"}

@app.post("/items/")
async def create_item(item: Item):
    return item.name