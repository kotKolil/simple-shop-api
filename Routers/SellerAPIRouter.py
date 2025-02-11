import sys

sys.path.append("..")

from fastapi import *
from fastapi.responses import *
from random import *

from Models.seller import *
from Models.models import *

SellerAPIRouter = APIRouter(prefix="/Seller")


@SellerAPIRouter.get(path="/", status_code=status.HTTP_200_OK)
async def getSeller(request: Request):
    IfAll = request.query_params("all", "0")
    if IfAll == "0":
        SellerId = request.query_params.get('id', "")
        SellerDataViaId = db.query(Seller).filter(Seller.id == SellerId).first()
        if not SellerDataViaId:
            return HTTPException(404)
        return JSONResponse(
            {
                "id": SellerDataViaId.id,
                "Name": SellerDataViaId.Name,
            }
        )
    elif IfAll == "1":
        SellerId = request.query_params.get('id', "")
        SellerDataViaId = db.query(Seller).filter(Seller.id == SellerId)
        if not SellerDataViaId:
            return HTTPException(404)
        return SellerDataViaId


@SellerAPIRouter.post(path="/", status_code=status.HTTP_201_CREATED)
async def createSeller(request: Request):
    try:
        requestJson = await request.json()
        SellerDataViaName = db.query(Seller).filter(Seller.Name == requestJson["name"]).first()
        if SellerDataViaName:
            return HTTPException(400)
        newSeller = Seller()
        newSeller.id = randint(10 ** 5, 10 ** 6)
        newSeller.Name = str(requestJson["name"])
        db.add(newSeller)
        db.commit()

        return JSONResponse(newSeller.as_dict())

    except KeyError:
        return HTTPException(400)


@SellerAPIRouter.patch(path="/", status_code=status.HTTP_200_OK)
async def editSeller(request: Request):
    try:
        requestJson = await request.json()
        Seller = db.query(Seller).filter(Seller.id == requestJson["id"]).first()
        if not Seller:
            return HTTPException(404)
        Seller.Name = requestJson["name"]
        db.commit()
        return HTTPException(200)
    except KeyError:
        return HTTPException(400)


@SellerAPIRouter.delete(path="/", status_code=status.HTTP_200_OK)
async def deleteSeller(request: Request):
    SellerId = request.query_params.get('id', "")
    Seller = db.query(Seller).filter(Seller.id == SellerId).first()
    if not Seller:
        return HTTPException(404)
    db.delete(Seller)
    db.commit()
    return HTTPException(200)
