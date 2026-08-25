from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    # FIX: Explicitly pass request, name, and context arguments
    return templates.TemplateResponse(
        request=request,
        name="index.html", 
        context={"request": request, "message": "Loaded via Bind Mount!"}
    )