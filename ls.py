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
async def create_message(user: User):
    if not users:
        user_id = 1
    else:
       user_id = users[-1].id + 1
    user.id = user_id
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
async def refresh(user_id: int, username: str, age: int, user: str = Body()):
    try:
        users[user_id].username = username
        users[user_id].age = age
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")

@app.delete("/user/{user_id}")
async def delete(user_id: int ) -> str:
    try:
        user = users.pop(user_id - 1)
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")








