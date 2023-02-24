import datetime
from fastapi import FastAPI, HTTPException, status
from typing import Optional
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()
users = []


class User(BaseModel):
    username: str
    password: str
    email: Optional[str]
    date_joined: datetime.date = datetime.date.today()



@app.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    users.append({"username": user.username, "password": user.password,
                  "email": user.email, "date_joined": user.date_joined})
    result = {"username": user.username, "email": user.email, "date_joined": user.date_joined}
    return result
