from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from . import settings

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return settings.TEMPLATES.TemplateResponse("homepage.html", {"request": request})

@app.get("/hello")
async def hello():
    return f"Hello, world!"

@app.get("/hello/{name}")
async def hello_name(name: str):
    return f"Hello, {name}!"