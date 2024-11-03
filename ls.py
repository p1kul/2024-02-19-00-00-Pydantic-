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
async def post_user(username: str, age: int, user: User):
    if not users:
        user_id = 1
    else:
       user_id = users[-1].id + 1
    user.id = user_id
    user.age = age
    user.username = username
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
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
     if user_id >= len(users) or user_id < 0:
         raise HTTPException(status_code=404, detail="User not found")
     del_user = users.pop(user_id - 1)
     return del_user


