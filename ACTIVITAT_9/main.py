from fastapi import FastAPI
from crud import read_users, insert_users, delete_users
import schemas

app = FastAPI()

# Para crear Usuaris


@app.post("/users")
async def create_users():
    insert_users()  # Calls the insert function to add users to the database
    return {"message": "Users added successfully"}

# Para llegir Usuaris


@app.get("/users", response_model=list[dict])
async def read_users_endpoint():
    users = read_users()  # Retorna users des de database
    return schemas.users_schema(users)

# Para Eliminar Usuaris


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    delete_users(user_id)  # Deletes the user by id
    return {"message": f"User with id {user_id} has been deleted"}

