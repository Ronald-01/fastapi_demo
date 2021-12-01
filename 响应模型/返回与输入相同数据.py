from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel,EmailStr

app=FastAPI()

class UserIn(BaseModel):
    name:str
    password:str
    email:EmailStr
    full_name:Optional[str]=None

@app.post("/user/",response_model=UserIn)
def create_user(user:UserIn):
    return user