from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()


# Employee model for normal responses
class Employee(BaseModel):
    employee_id: int
    name: str
    department: str
    position: str
    start_date: str
    salary: float | None = None


data_employee = {
    1: {
        "employee_id": 1,
        "name": "Brandy",
        "department": "IT",
        "position": "Intern",
        "start_date": "2023-01-01",
        "salary": 0
    }
}


@app.get("/")
async def root():
    return {"Activitat FastApi"}


@app.post("/employee/")
async def create_item(employee: Employee):
    return {"employee": employee}


@app.get("/employee/{employee_id}")
async def get_employee(employee_id: int):
    employee = data_employee.get(employee_id)

    if not employee:
        return JSONResponse(status_code=404, content={"detail": "Employee not found"})

    return {"employee": employee}


