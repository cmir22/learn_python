from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestFormStrict

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="/login")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "cmir": {
        "username": "cmir22",
        "full_name": "cruz ibarra",
        "email": "cmir@hotmail.com",
        "disabled": False,
        "password": "23213ed12d"
    },
    "cmir2": {
        "username": "cmir222",
        "full_name": "cruz ibarra2",
        "email": "cmir@hotmail.com",
        "disabled": True,
        "password": "weg2fof"
    }
}


def search_user(username: str):
    if (username in users_db):
        return UserDB(users_db[username])


@app.post("/login")
async def login(form: OAuth2PasswordRequestFormStrict = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="Incorrect user")

    user = search_user(form.username)
    if not (form.password == user.password):
        raise HTTPException(status_code=400, detail="Incorrect user")

    return {"acces_token": user.username, "token type": "bearer"}


# Get users
@app.get("/users/")
async def me(user: User = Depends()):
    return user
