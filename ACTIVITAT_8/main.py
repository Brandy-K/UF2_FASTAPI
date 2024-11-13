## rsobrinog
from fastapi import FastAPI
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Activitat FastApi"}


