from fastapi import FastAPI
from routers import contact

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# パッケージ内のルーター（インスタンス）を読み込み
app.include_router(contact.router)