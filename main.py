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


# index page endpoint
@app.get("/")
def root():
    return HTMLResponse("It works!")
