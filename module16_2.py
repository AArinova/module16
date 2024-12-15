from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Главная страница."}

@app.get("/user/admin")
async def admin():
    return {"message": "Вы вошли как администратор."}

@app.get("/users/{user_id}")
async def get_user_by_id(
    user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")]):
    return {"user_id": user_id}

@app.get("/users/{username}")
async def get_user_by_username(
    username: Annotated[str, Path(min_length=5, max_length=20, regex="^[a-zA-Z0-9_-]+$")]
    ):
    return {'username' : username}

@app.get("/user/{username}/{age}")
async def get_user_info(
    username: Annotated[str, Path(min_length=5, max_length=20, regex="^[a-zA-Z0-9_-]+$", description="Enter username")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
    ):
    return {"Имя": {username}, "Возраст": {age}}




