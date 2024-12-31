#importing libraries
from fastapi import *
from fastapi.responses import *
from sqlalchemy import create_engine
from Models.models import Base

#defining app variable
app = FastAPI()

#index page endpoint
@app.get("/")
def index(request: Request):
    return HTMLResponse("It works!")

