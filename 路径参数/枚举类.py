from enum import Enum
from fastapi import FastAPI
class ModelName(str,Enum):
    cp="123"
    dd="111"

app=FastAPI()

@app.get("/models/{name}")
async  def get_model(name:ModelName):
    if name==ModelName.cp:
        return {"model_name":name,"message":"44"}
