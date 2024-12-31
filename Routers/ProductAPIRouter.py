import sys

sys.path.append("..")

from fastapi import *
from fastapi.responses import *
from Models.models import *
from random import *

ProductAPIController = APIRouter(prefix="product")

@ProductAPIController.get(status_code = status.HTTP_200_OK )
def getSeller(request: Request):
    ProductId = request.query_params.get('id', "").first()
    ProductData = db.filter(product.id == ProductId)
    return JSONResponse(
        {
            "id": ProductData.id,
            "shopId": ProductData.shopId,
            "price": ProductData.price,
            "Name": ProductData.Name,
        }
    )

@ProductAPIController.post(status_code = status.HTTP_201_CREATED)
def createSeller(request:Request):
    requestJson = request.json()

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


@ProductAPIController.patch(status_code = status.HTTP_200_OK)
def editProduct(request:Request):
    requestJson = request.json()

    newProduct = shop()
    newProduct.Name = requestJson["Name"] if 'Name' in requestJson and requestJson["Name"] \
                                          and isinstance(requestJson["Name"], str) else newProduct.Name
    newProduct.shopId = requestJson["shopId"] if 'shopId' in requestJson and requestJson["shopId"] \
                                          and isinstance(requestJson["shopId"], str) else newProduct.shopId
    newProduct.price = requestJson["price"] if 'price' in requestJson and requestJson["price"] \
                                      and isinstance(requestJson["price"], str) else newProduct.price
    db.add(newProduct)
    db.commit()

@ProductAPIController.delete(status_code = status.HTTP_200_OK)
def deleteProduct(request:Request):
    requestJson = request.json()
    if requestJson["id"]:
        Product = product.filter(id == requestJson["id"]).first()
        db.delete(Product)
        db.commit()
    else:
        return JSONResponse(["400"], status_code=status.HTTP_400_BAD_REQUEST)