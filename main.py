from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/sum", response_class=HTMLResponse)
async def calculate_sum(request: Request, a: int = Form(...), b: int = Form(...)):
    result = a + b
    return templates.TemplateResponse("result.html", {"request": request, "a": a, "b": b, "result": result})
