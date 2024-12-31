import sys

sys.path.append("..")

from fastapi import *
from fastapi.responses import *
from Models.models import *
from random import *

SellerAPIRouter = APIRouter(prefix="seller")

@SellerAPIRouter.get(status_code = status.HTTP_200_OK )
def getSeller(request: Request):
    SellerId = request.query_params.get('id', "").first()
    SellerData = db.filter(seller.id == SellerId)
    return JSONResponse(
        {
            "id": SellerData.id,
            "Name": SellerData.Name,
        }
    )

@SellerAPIRouter.post(status_code = status.HTTP_201_CREATED)
def createSeller(request:Request):
    requestJson = request.json()

    newSeller = shop()
    newSeller.id = randint(10**5, 10**6)
    newSeller.Name = requestJson["Name"] if 'Name' in requestJson and requestJson["Name"] \
                                          and isinstance(requestJson["Name"], str) else None
    db.add(newSeller)
    db.commit()


@SellerAPIRouter.patch(status_code = status.HTTP_200_OK)
def editSeller(request:Request):
    requestJson = request.json()
    if requestJson["id"]:
        Seller= seller.filter(id == requestJson["id"]).first()
    else:
        return JSONResponse(["400"], status_code=status.HTTP_400_BAD_REQUEST)
    Seller.Name = requestJson["Name"] if 'Name' in requestJson and requestJson["Name"] \
                                       and isinstance(requestJson["Name"], str) else Seller.Name
    db.commit()

@SellerAPIRouter.delete(status_code = status.HTTP_200_OK)
def deleteSeller(request:Request):
    requestJson = request.json()
    if requestJson["id"]:
        Seller = seller.filter(id == requestJson["id"]).first()
        db.delete(Seller)
        db.commit()
    else:
        return JSONResponse(["400"], status_code=status.HTTP_400_BAD_REQUEST)