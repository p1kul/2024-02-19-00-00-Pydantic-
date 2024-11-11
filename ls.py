from fastapi import FastAPI,Path, status, Body, HTTPException
from pydantic import BaseModel
app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/users")
async def all_inf():
    return users

@app.post("/user/{username}/{age}")
async def post_user(user: User):
    if not users:
        user.id = 1
    else:
        user.id = users[-1].id + 1
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
async def refresh_user(user_id: int, username: str, age: int, user: str = Body()):
    try:
        refresh = users[user_id - 1]
        refresh.username = username
        refresh.age = age
        return refresh
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
     rul = users[user_id - 1]
     if  user_id < 0 or rul.id != user_id:
         raise HTTPException(status_code=404, detail="User was not found")
     del_user = users.pop(user_id - 1)
     return del_user


