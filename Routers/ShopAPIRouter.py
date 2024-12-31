import sys

sys.path.append("..")

from fastapi import *
from fastapi.responses import *
from Models.models import *
from random import *

ShopAPIRouter = APIRouter(prefix="shop")

@ShopAPIRouter.get(status_code = status.HTTP_200_OK )
def getShop(request: Request):
    ShopId = request.query_params.get('ShopId', "").first()
    shopData = db.filter(shop.id == ShopId)
    return JSONResponse(
        {
            "id": shopData.id,
            "SellerId": shopData.SellerId,
            "Name": shopData.Name,
            "numOfProducts": shopData.numOfProducts,
            "Address": shopData.Adress
        }
    )

@ShopAPIRouter.post(status_code = status.HTTP_201_CREATED)
def createShop(request:Request):
    requestJson = request.json()

    newShop = shop()
    newShop.id = randint(10**5, 10**6)
    newShop.SellerId = requestJson["SellerId"] if "SellerId" in requestJson and requestJson["SellerId"] \
                                                  and isinstance(requestJson["SellerId", int]) else None
    newShop.Name = requestJson["Name"] if 'Name' in requestJson and requestJson["Name"] \
                                          and isinstance(requestJson["Name"], str) else None
    newShop.Address = requestJson["Address"] if "Address" in requestJson and requestJson["Address"] \
                                                and isinstance(requestJson["Adress"], str) else None

    db.add(newShop)
    db.commit()


@ShopAPIRouter.patch(status_code = status.HTTP_200_OK)
def editShop(request:Request):
    requestJson = request.json()
    if requestJson["id"]:
        Shop = shop.filter(id == requestJson["id"]).first()
    else:
        return JSONResponse(["400"], status_code=status.HTTP_400_BAD_REQUEST)
    Shop.SellerId = requestJson["SellerId"] if "SellerId" in requestJson and requestJson["SellerId"] \
                                               and isinstance(requestJson["SellerId", int]) else Shop.SellerId
    Shop.Name = requestJson["Name"] if 'Name' in requestJson and requestJson["Name"] \
                                       and isinstance(requestJson["Name"], str) else Shop.name
    Shop.Address = requestJson["Address"] if "Address" in requestJson and requestJson["Address"] \
                                                and isinstance(requestJson["Adress"], str) else Shop.Adress
    db.commit()

@ShopAPIRouter.delete(status_code = status.HTTP_200_OK)
def deleteShop(request:Request):
    requestJson = request.json()
    if requestJson["id"]:
        Shop = shop.filter(id == requestJson["id"]).first()
        db.delete(Shop)
        db.commit()
    else:
        return JSONResponse(["400"], status_code=status.HTTP_400_BAD_REQUEST)