from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

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
            <h3 style="margin-top: 100px">If you want a warmer welcome, add your name to the end of the URL</h3>
            <p>(for example http://127.0.0.1:8000/John)</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/{name}", response_class=HTMLResponse)
async def greet(request: Request, name: str):
    return templates.TemplateResponse("greet.html", {"request": request, "name": name.capitalize()})
