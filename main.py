from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    html_content = """
    <html>
        <head>
            <title>Root</title>
        </head>
        <body style='text-align: center'>
            <h1 style="margin-top:50px">Welcome to FastAPI</h1>
            <h2>a Python framework</h2>
            <h3 style="margin-top: 100px">For a warmer welcome, add your name to the end of the URL</h3>
            <p>(for example http://localhost:8000/John)</p>
            
            <img src="static/fastapi-logo.png" alt="fast api logo">
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/{name}", response_class=HTMLResponse)
async def greet(request: Request, name: str):
    return templates.TemplateResponse("greet.html", {"request": request, "name": name.capitalize()})
