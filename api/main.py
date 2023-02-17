from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
async def homepage():
    time = datetime.datetime.now()
    return f"The time is {time}"

@app.get("/hello")
async def hello():
    return f"Hello, world!"

@app.get("/hello/{name}")
async def hello_name(name: str):
    return f"Hello, {name}!"