from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi import HTTPException , status
app = FastAPI()


users = {
    1 : {
        "name": "Alice",
        "age": 30
    }
}

class User(BaseModel):
    id: Optional[int] = None
    name: str
    age: int    

@app.get("/")
def root():
    return {"message": "welcome to learn FastAPI"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id in users:
        return users[user_id]

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"user with id {user_id} not found")

@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(user: User,user_id: int):
        if user_id not in users:
            users[user_id] = user.dict()
            return users[user_id]
        else:
            raise HTTPException(status_code=status.HTTP_302_FOUND,
                        detail=f"user with id {user.id} already exists")
            
    


