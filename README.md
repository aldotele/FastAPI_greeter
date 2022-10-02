# FastAPI Greeter
This small server is built with FastAPI Python Framework.\
It currently uses two endpoints:
- */* shows a generic welcome message
- */{your_name}* will show a customized welcome message based on the name you pass it

## How to Launch

### with Docker
type on terminal:
1) `docker build -t {your_image_name} .`
2) `docker run -it -p 8000:8000 --name {your_container_name} {your_image_name}`

navigate to [localhost:8000](http://localhost:8000)

### with Python
With Python3 installed on your local machine, open your CLI and do the following steps:
- create virtual environment (optional but recommended)
- type `pip install -r requirements.txt`
- type `uvicorn main:app`  (to launch the server)
- navigate to [localhost:8000](http://localhost:8000)