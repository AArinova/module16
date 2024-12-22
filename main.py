from fastapi.exceptions import HTTPException
from fastapi import Request, FastAPI, Path
from pydantic import BaseModel, Field
from typing import List, Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")
#app = FastAPI()
app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)

class User(BaseModel):
    id: int
    username: str
    age: int

class UserCreate(BaseModel):
    username: str = Field(..., min_length=5, max_length=100)
    age: int = Field(..., ge=18, le=120)

users: List[User]=[User(id=1, username='Example', age=22)]

@app.get("/", response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.post("/user/{username}/{age}", response_model=User)
async def create_user(user: UserCreate):
    new_id = max((t.id for t in users), default=0) + 1
    new_user = User(id=new_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(user_id: int, user: UserCreate):
    for i_user in users:
        if i_user.id == user_id:
            i_user.username = user.username
            i_user.age = user.age
            return i_user
    raise HTTPException(status_code=404, detail="Нет пользователя с таким id.")

@app.delete("/user/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    for i, i_user in enumerate(users):
        if i_user.id == user_id:
            del users[i]
            return {"detail": "Пользователь удалён."}
    raise HTTPException(status_code=404, detail="User was not found")










