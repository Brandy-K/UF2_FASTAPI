from fastapi import FastAPI
from pydantic import BaseModel

import users
app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    surname: str


@app.get("/users", response_model=list[dict])
async def read_users():
    return users.users_schema(users.read())
