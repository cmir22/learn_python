from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return "Hello world"


@app.get('/url')
async def root2():
    return {"url_course": "google.com"}
