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
            "Name": ProductData.Name,
        }
    )

@ProductAPIController.post(path =  "/", status_code = status.HTTP_201_CREATED)
async def createSeller(request:Request):
    requestJson = await request.json()

    newProduct = shop()
    newProduct.id = randint(10**5, 10**6)
    newProduct.Name = requestJson["Name"] if 'Name' in requestJson and requestJson["Name"] \
                                          and isinstance(requestJson["Name"], str) else None
    newProduct.shopId = requestJson["shopId"] if 'shopId' in requestJson and requestJson["shopId"] \
                                          and isinstance(requestJson["shopId"], str) else None
    newProduct.price = requestJson["price"] if 'price' in requestJson and requestJson["price"] \
                                      and isinstance(requestJson["price"], str) else None
    db.add(newProduct)
    db.commit()
    return HTTPException(200)

@ProductAPIController.patch(path =  "/", status_code = status.HTTP_200_OK)
async def editProduct(request:Request):
    requestJson = await request.json()
    oldProduct = db.query(product).filter(product.id == requestJson["id"]).first()
    if not oldProduct:
        return HTTPException(404)
    oldProduct.Name = requestJson["Name"] if 'Name' in requestJson and requestJson["Name"] \
                                          and isinstance(requestJson["Name"], str) else oldProduct.Name
    oldProduct.shopId = requestJson["shopId"] if 'shopId' in requestJson and requestJson["shopId"] \
                                          and isinstance(requestJson["shopId"], str) else oldProduct.shopId
    oldProduct.price = requestJson["price"] if 'price' in requestJson and requestJson["price"] \
                                      and isinstance(requestJson["price"], str) else oldProduct.price
    db.query(product).add(oldProduct)
    db.commit()
    return HTTPException(200)

@ProductAPIController.delete(path =  "/", status_code = status.HTTP_200_OK)
async def deleteProduct(request: Request):
    requestJson = await request.json()
    Product = db.query(product).filter(id == requestJson["id"]).first()
    if not Product:
        return HTTPException(404)
    db.delete(Product)
    db.commit()
    return HTTPException(200)