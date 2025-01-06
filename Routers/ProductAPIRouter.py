import sys

sys.path.append("..")

from fastapi import *
from fastapi.responses import *
from Models.models import *
from random import *

ProductAPIController = APIRouter(prefix="/product")

@ProductAPIController.get(path =  "/", status_code = status.HTTP_200_OK )
async def getSeller(request: Request):
    ProductId = request.query_params.get('id', "")
    ProductData = db.query(product).filter(product.id == ProductId).first()
    if not ProductData:
        return HTTPException(404)
    return JSONResponse(
        {
            "id": ProductData.id,
            "shopId": ProductData.shopId,
            "price": ProductData.price,
            "Name": ProductData.name,
        }
    )

@ProductAPIController.get(path =  "/all", status_code = status.HTTP_200_OK )
async def allShop(request:Request):
    return db.query(product).all()


@ProductAPIController.post(path =  "/", status_code = status.HTTP_201_CREATED)
async def createSeller(request:Request):

    try:

        requestJson = await request.json()

        newProduct = product()
        newProduct.id = randint(10**5, 10**6)
        newProduct.name = requestJson["name"]
        newProduct.shopId = requestJson["ShopId"]
        newProduct.price = requestJson["price"]
        db.add(newProduct)
        db.commit()
        return HTTPException(200)

    except KeyError:
        return HTTPException(400)

@ProductAPIController.patch(path =  "/", status_code = status.HTTP_200_OK)
async def editProduct(request:Request):
    try:
        requestJson = await request.json()
        oldProduct = db.query(product).filter(product.id == requestJson["id"]).first()
        if not oldProduct:
            return HTTPException(404)
        oldProduct.name = requestJson["name"]
        oldProduct.shopId = requestJson["ShopId"]
        oldProduct.price = requestJson["price"]
        db.add(oldProduct)
        db.commit()
        return HTTPException(200)
    except KeyError:
        return HTTPException(400)

@ProductAPIController.delete(path =  "/", status_code = status.HTTP_200_OK)
async def deleteProduct(request: Request):
    requestJson = await request.json()
    Product = db.query(product).filter(product.id == requestJson["id"]).first()
    if not Product:
        return HTTPException(404)
    db.delete(Product)
    db.commit()
    return HTTPException(200)

