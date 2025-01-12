# importing libraries
from Routers.ShopAPIRouter import *
from Routers.SellerAPIRouter import *
from Routers.ProductAPIRouter import *

# defining app variable
app = FastAPI()

# connecting routers to main app
app.include_router(ShopAPIRouter)
app.include_router(SellerAPIRouter)
app.include_router(ProductAPIController)

#creating authorization middleware
@app.middleware("http")
async def authorization_middleware(request:Request, call_next):
    json_data = request.json()
    if request.url.path == "/" or request.url.path == "/user":
        response = await call_next(request)
        return response
    return "403"

# index page endpoint
@app.get("/")
def root():
    return HTMLResponse("It works!")
