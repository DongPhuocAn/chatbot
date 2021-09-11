from fastapi import FastAPI, Form
from chatgui import getList, getList2
from tkinter import *
import uvicorn
from pydantic import BaseModel
from typing import Optional, List, Any
app = FastAPI()

mylist = getList()
mylist2 = getList2()

db = []
class Item(BaseModel):
    name: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/bot")
def get_bot_response():
    return ({"chatbot": str(mylist)})

@app.get("/user")
def get_bot_response():
    return ({"chatbot": str(mylist2)})

@app.get("/items/")
def get_item():
    return db
@app.post("/items/")
def create_item(item: Item):
    db.append(item.dict())
    return db[-1]



if __name__ == '__main__':
    uvicorn.run(app)