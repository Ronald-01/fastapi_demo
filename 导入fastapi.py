import uvicorn
from fastapi import FastAPI

app = FastAPI()


# 添加首页
@app.get("/")
def index():
    return "this is home page"


if __name__ == '__main__':
    uvicorn.run(app)
