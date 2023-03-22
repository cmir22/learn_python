from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User():
    username: str
    full_name: str
    surname: str
    disabled: bool


class UserDB():
    password: str


users_db = {
    "cmir": {
        "username": "cmir22",
        "full_name": "cruz ibarra",
        "emial": "cmir@hotmail.com",
        "disabled": False,
        "password": "23213ed12d"
    },
    "cmir2": {
        "username": "cmir222",
        "full_name": "cruz ibarra2",
        "emial": "cmir@hotmail.com",
        "disabled": True,
        "password": "weg2fof"
    }
}
