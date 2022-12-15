# server.py
from fastapi import FastAPI
from app.database import addUser

from app.route.models import User

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello WocxsaxZrld"}

@app.post("/signup")
async def signup(Fname:str , Lname:str , phone:str):
    addUser(Fname,Lname,phone)

    