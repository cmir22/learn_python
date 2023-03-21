from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User():
    id: int
    name: str
    surname: str
    url: str
    age: int


users = []


@app.get('/user/{id}')
async def user(id: int):
    return User()


@app.post('/user/{id}')
async def user(id: int):
    return User()
