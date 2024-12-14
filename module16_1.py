from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#class User(BaseModel):
#    username: str
#    age: int

@app.get("/")
async def root():
    return {"message": "Кажется, это главная страница."}

@app.get("/user/admin")
async def admin():
    return {"message": "Вы вошли как администратор."}

@app.get("/user/{user_id}")
async def check_user(user_id: int):
    return {f"Вы вошли как пользователь № {user_id}."}

@app.get("/user")
async def get_user_info(uname: str, age: int):
    return {f"Информация о пользователе. Имя: {uname}, Возраст: {age}."}


