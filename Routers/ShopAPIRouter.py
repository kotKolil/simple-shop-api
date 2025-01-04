import sys

sys.path.append("..")

from fastapi import *
from fastapi.responses import *
from Models.models import *
from random import *

ShopAPIRouter = APIRouter(prefix="/shop")

@ShopAPIRouter.get(path =  "/", status_code = status.HTTP_200_OK )
async def getShop(request: Request):
    ShopId = request.query_params.get('id', "")
    shopData = db.query(shop).filter(shop.id == ShopId).first()
    if not shopData:
        return HTTPException(404)
    return shopData

@ShopAPIRouter.get(path =  "/all", status_code = status.HTTP_200_OK )
async def allShop(request:Request):
    return db.query(shop).all()

@ShopAPIRouter.post(path =  "/", status_code = status.HTTP_201_CREATED)
async def createShop(request: Request):
    try:
        request_json = await request.json()

        new_shop = shop()
        new_shop.id = randint(10 ** 5, 10 ** 6)
        new_shop.SellerId = request_json["SellerId"]
        new_shop.Name = request_json["name"]
        new_shop.Address = request_json["address"]

        db.add(new_shop)
        db.commit()

        return HTTPException(200)

    except KeyError:
        return HTTPException(400)


@ShopAPIRouter.patch(path =  "/", status_code = status.HTTP_200_OK)
async def editShop(request:Request):
    try:
        requestJson = await request.json()
        Shop = db.query(shop).filter(shop.id == requestJson["id"]).first()
        if not Shop:
            return HTTPException(404)
        Shop.SellerId = requestJson["SellerId"]
        Shop.Name = requestJson["name"]
        Shop.Address = requestJson["address"]
        db.commit()

        return HTTPException(200)
    except KeyError:
        return HTTPException(400)

@ShopAPIRouter.delete(path =  "/", status_code = status.HTTP_200_OK)
async def deleteShop(request:Request):
    requestJson = await request.json()
    Shop = shop.filter(id == requestJson["id"]).first()
    if not Shop:
        return HTTPException(404)
    db.delete(Shop)
    db.commit()
    return HTTPException(200)
