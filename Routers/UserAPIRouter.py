from fastapi import *
from fastapi.responses import *

from Models.models import *
from Models.user import *

from users.auth import *
from users.tokens import *

UserAPIController = APIRouter(prefix="user")


@UserAPIController.get()
async def getToken(request: Request) -> Response:
    request_data = request.json()
    username = request_data["username"]
    hashed_password = get_password_hash(request_data["password"])
    userFromDB = db.query(User).filter(User.id == username).first()
    if userFromDB.pasword == hashed_password and userFromDB:
        return JSONResponse(hashed_password)
    return HTTPException(status_code=401, detail="wrong password or username")


@UserAPIController.post()
async def createUser(request: Request) -> Response:
    request_data = request.json()
    username = request_data["username"]
    hashed_password = get_password_hash(request_data["password"])
    userFromDB = db.query(User).filter(User.id == username and User.password == hashed_password).first()
    if userFromDB:
        return HTTPException(status_code=400, detail="user or password are now using")
    newUser = User()
    newUser.id = username
    newUser.password = hashed_password
    db.add(newUser)
    db.commit()
    return JSONResponse(
        {
            "username": username,
            "password": request_data["password"],
            'token': create_access_token(username)
        }
    )