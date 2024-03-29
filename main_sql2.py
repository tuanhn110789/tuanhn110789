
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from a2wsgi import ASGIMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
   return templates.TemplateResponse('Main1.html', {"request": request})

        
wsgi_app = ASGIMiddleware(app)
