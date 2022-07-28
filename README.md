# FastAPI Greeter
This small server is built with FastAPI Python Framework.\
It currently uses two endpoints:
- */* shows a generic welcome message
- */{your_name}* will show a customized welcome message based on the name you pass it

## How to launch
With Python3 installed on your local machine, open your CLI and do the following steps:
- create virtual environment (optional but recommended)
- type `pip install -r requirements.txt`
- type `uvicorn main:app`  (to launch the server)
- navigate to [localhost:8000](localhost:8000) to see first endpoint
- navigate to [localhost:8000/{your_name}](localhost:8000/John Doe) to see second endpoint