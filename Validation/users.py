from pydantic import BaseModel


class Users(BaseModel):
    user_id: int
    user_name: str
    user_type: int
