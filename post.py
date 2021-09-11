from fastapi import FastAPI, Form
from tkinter import *
import uvicorn
from pydantic import BaseModel
from typing import Optional, List, Any
app = FastAPI()
db = []


app = FastAPI()
@app.get("/items/")
def get_item():
    return db
@app.post("/items/{file_path:path")
def create_item(item: str):
    db.append(item)
    return db[-1]


if __name__ == '__main__':
    uvicorn.run(app)