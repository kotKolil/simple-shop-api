# importing libraries
from Routers.ShopAPIRouter import *
from Routers.SellerAPIRouter import *
from Routers.ProductAPIRouter import *

from users.auth import *
from users.auth import *

# defining app variable
app = FastAPI()

# connecting routers to main app
app.include_router(ShopAPIRouter)
app.include_router(SellerAPIRouter)
app.include_router(ProductAPIController)

#creating authorization middleware
@app.middleware("http")
async def authorization_middleware(request: Request, call_next):
    if await request.method == "GET":
        response = await call_next(request)
        return response
    else:
        json_data = await request.json()
        if request.url.path == "/" or request.url.path == "/user":
            response = await call_next(request)
            return response
        if "access_token" not in json_data:
            return HTTPResponse(403)
        user_data = decode(json_data["access_token"])
        if user_data != json_data["OwnerId"]:
            return HTTPResponse(403)
        response = await call_next(request)
        return response


# index page endpoint
@app.get("/")
def root():
    return HTMLResponse("It works!")
