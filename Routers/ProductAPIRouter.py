import sys

sys.path.append("..")

from fastapi import *
from fastapi.responses import *
from random import *

from Models.models import *
from Models.product import *

ProductAPIController = APIRouter(prefix="/Product")


@ProductAPIController.get(path="/", status_code=status.HTTP_200_OK)
async def getSeller(request: Request):
    IfAll = request.query_params.get("all", "0")
    if IfAll == "0":
        ProductId = request.query_params.get('id', "")
        ProductData = db.query(Product).filter(Product.id == ProductId).first()
        if not ProductData:
            return HTTPException(404)
        return JSONResponse(
            {
                "id": ProductData.id,
                "shopId": ProductData.shopId,
                "price": ProductData.price,
                "name": ProductData.name,
            }
        )
    elif IfAll == "1":
        ProductId = request.query_params.get('id', "")
        ProductData = db.query(Product).filter(Product.id == ProductId)
        if not ProductData:
            return HTTPException(404)
        return ProductData


@ProductAPIController.post(path="/", status_code=status.HTTP_201_CREATED)
async def createSeller(request: Request):
    try:

        requestJson = await request.json()

        newProduct = Product()
        newProduct.id = randint(10 ** 5, 10 ** 6)
        newProduct.name = requestJson["name"]
        newProduct.shopId = requestJson["ShopId"]
        newProduct.price = requestJson["price"]
        db.add(newProduct)
        db.commit()
        return JSONResponse(newProduct.as_dict())

    except KeyError:
        return HTTPException(400)


@ProductAPIController.patch(path="/", status_code=status.HTTP_200_OK)
async def editProduct(request: Request):
    try:
        requestJson = await request.json()
        oldProduct = db.query(Product).filter(Product.id == requestJson["id"]).first()
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


@ProductAPIController.delete(path="/", status_code=status.HTTP_200_OK)
async def deleteProduct(request: Request):
    requestJson = request.query_params.get('id', "")
    Product = db.query(Product).filter(Product.id == requestJson).first()
    if not Product:
        return HTTPException(404)
    db.delete(Product)
    db.commit()
    return HTTPException(200)
