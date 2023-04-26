from fastapi import FastAPI


app = FastAPI(title="FastApi")

users = [
    {"id": 1, "name": "Andrei"},
    {"id": 2, "name": "NeAndrei"}
]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in users if user.get("id") == user_id]


@app.get("/users/")
def get_users(limit: int = 1, offset: int = 0):
    return users[offset:][:limit]


@app.post("/users/{user_id}")
def change_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user["id"] == user_id, users))[0]
    current_user["name"] = new_name
    return {"status_code": 200, "data": current_user}