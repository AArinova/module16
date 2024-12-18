from http.client import HTTPException
from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    age: int

users: List[User]=[User(id =1, username='Example', age =18)]

@app.get("/user", response_model=List[User])
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def add_user(username: Annotated[str, Path(min_length=5, max_length=20, regex="^[a-zA-Z0-9_-]+$", description="Enter username")],
                   age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
                   ):
    new_user_id = int(max(users, key=users.get))+1
    users[new_user_id] = f"Имя: {username}, возраст: {str(age)}"
    return f"User {new_user_id} is registered."

Добавляет в список users объект User.
id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
Все остальные параметры объекта User - переданные в функцию username и age соответственно.
В конце возвращает созданного пользователя.

@app.put("/user/{user_id}/{username}/{age}")
async def add_user(username: Annotated[str, Path(min_length=5, max_length=20, regex="^[a-zA-Z0-9_-]+$", description="Enter username")],
                   user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")],
                   age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
                   ):
    if user_id not in users.keys():
        """Переопределяем"""
        users[user_id] = f"Имя: {username}, возраст: {age}"
    else:
        raise HTTPException(detail="Уже есть такой пользователь.")
    return f"The user {user_id} is updated."

@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")]):
    if user_id in users.keys():
        del users[user_id]
    else:
        raise HTTPException(status_code=404, detail=f"пользователь с id={user_id} не найден.")
    return f"Пользователь {user_id} удален."







