from fastapi import FastAPI
from Database import Database
from Validation.users import Users
from pydantic import BaseModel
from typing import List


app = FastAPI(title="FastApi")
db = Database()


@app.on_event("startup")
async def startup():
    db.connect()


@app.on_event("shutdown")
async def shutdown():
    db.disconnect()


@app.get("/users/{user_id}", response_model=List[Users])
def get_user(user_id: int):
    data = db.select_query(f"SELECT * FROM users where user_id = {user_id}")
    if [user for user in data if user['user_id'] == user_id]:
        return data


@app.get("/users/")
def get_users(limit: int = 1, offset: int = 0):
    result = db.select_query(f"SELECT * FROM users")
    return result[offset:][:limit]


@app.post("/users/{user_id}")
def change_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user["id"] == user_id, users))[0]
    current_user["name"] = new_name
    return {"status_code": 200, "data": current_user}
