import sys

sys.path.append("..")

from fastapi import *
from fastapi.responses import *
from Models.models import *
from random import *

ShopAPIRouter = APIRouter(prefix="/shop")

@ShopAPIRouter.get(path =  "/", status_code = status.HTTP_200_OK )
async def getShop(request: Request):
    ShopId = request.query_params.get('ShopId', "").first()
    shopData = db.filter(shop.id == ShopId)
    if shopData:
        return HTTPException(404)
    return JSONResponse(
        {
            "id": shopData.id,
            "SellerId": shopData.SellerId,
            "Name": shopData.Name,
            "numOfProducts": shopData.numOfProducts,
            "Address": shopData.Adress
        }
    )

@ShopAPIRouter.post(path =  "/", status_code = status.HTTP_201_CREATED)
async def createShop(request:Request):
    requestJson = await request.json()

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

    return HTTPException(200)


@ShopAPIRouter.patch(path =  "/", status_code = status.HTTP_200_OK)
async def editShop(request:Request):
    requestJson = await request.json()
    Shop = shop.filter(id == requestJson["id"]).first()
    if Shop:
        return HTTPException(404)
    Shop.SellerId = requestJson["SellerId"] if "SellerId" in requestJson and requestJson["SellerId"] \
                                               and isinstance(requestJson["SellerId", int]) else Shop.SellerId
    Shop.Name = requestJson["Name"] if 'Name' in requestJson and requestJson["Name"] \
                                       and isinstance(requestJson["Name"], str) else Shop.name
    Shop.Address = requestJson["Address"] if "Address" in requestJson and requestJson["Address"] \
                                                and isinstance(requestJson["Adress"], str) else Shop.Adress
    db.commit()

    return HTTPException(200)
@ShopAPIRouter.delete(path =  "/", status_code = status.HTTP_200_OK)
async def deleteShop(request:Request):
    requestJson = await request.json()
    Shop = shop.filter(id == requestJson["id"]).first()
    if not Shop:
        return HTTPException(404)
    db.delete(Shop)
    db.commit()
    return HTTPException(200)
