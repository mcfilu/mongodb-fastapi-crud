from fastapi import FastAPI
from pydantic import BaseModel
from routers import users



app = FastAPI()

app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Welcome to mongodb-fastapi-crud application. Please refer to /docs to see more details"}



