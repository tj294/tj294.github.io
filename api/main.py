from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def homepage():
    return f"<h1>Hello, world!</h1>"

@app.get("/hello")
async def hello():
    return f"Hello, world!"

@app.get("/hello/{name}")
async def hello_name(name: str):
    return f"Hello, {name}!"