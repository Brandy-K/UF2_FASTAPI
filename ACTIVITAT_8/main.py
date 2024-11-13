from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

# Employee model for normal responses
class Employee(BaseModel):
    employee_id: int
    name: str
    department: str
    position: str
    start_date: str
    salary: float | None = None

@app.get("/")
async def root():
    return {"Activitat FastApi"}

@app.post("/employee/")
async def create_item(employee: Employee):
    return {"employee": employee}



