from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    name: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    name: str
    email: EmailStr
    full_name: Optional[str] = None


# FastAPI会用Pydantic过滤掉未在UserOut中声明的数据
@app.post("/user/", response_model=UserOut)
def create_user(user: UserIn):
    return user
