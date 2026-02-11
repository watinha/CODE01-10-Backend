from datetime import datetime


from pydantic import BaseModel


class UserQuery(BaseModel):
    username: str


class UserCreate(BaseModel):
    username: str
    password: str
    created_at: datetime


