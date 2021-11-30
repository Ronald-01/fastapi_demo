import uvicorn
from fastapi import FastAPI
from pydantic import  BaseModel

class Item(BaseModel):
    name: str="201902010214"
    description:str="学号"
    psw: str="1234"

app = FastAPI()


@app.api_route("/login", methods=("GET", "POST", "PUT"))
def login():
    return {"msg": "login success"}
