from fastapi import FastAPI
from pydantic import BaseModel

class Employee(BaseModel):
    employee_id: int
    name: str
    department: str
    position: str
    start_date: str
    salary: float | None = None

app = FastAPI()

@app.get("/employee/")
async def get_employee(employee_id: int, name: str, department: str, position: str, start_date: str, salary: float | None = None):
    employee = Employee(
        employee_id=employee_id,
        name=name,
        department=department,
        position=position,
        start_date=start_date,
        salary=salary
    )
    return {"employee": employee}

