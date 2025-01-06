import sys

sys.path.append("..")

from fastapi.testclient import TestClient
from main import *

client = TestClient(app)

global simple_seller_data
simple_seller_data = {
    "name": "sample seller"
}


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_CreateMethodSellerAPIRouter():
    # creating test seller
    response = client.post(
        "/seller/",
        json={
            "name": simple_seller_data["name"]
        },
    )
    assert response.status_code == 201


def test_AllMethodSellerAPIRouter():
    # getting all sellers from DB
    response = client.get(
        "/seller/all",
    )
    assert response.status_code == 200
    for i in response.json():
        if i["Name"] == simple_seller_data["name"]:
            simple_seller_data["id"] = i["id"]


def test_GetMethodSellerAPIRouter():
    # testing data acess via id
    response = client.get(f"/seller/?id={simple_seller_data["id"]}")
    assert response.json()["Name"] == simple_seller_data["name"]
    assert response.json()["id"] == simple_seller_data["id"]


def test_PatchMethodSellerAPIRouter():
    # testing editing data in DB via api
    response = client.patch(
        "/seller",
        json={
            "id": simple_seller_data['id'],
            "name": "sample seller 2"
        }
    )
    assert response.status_code == 200
    simple_seller_data["name"] = "sample seller 2"


def test_DeleteMethodAPIRouter():
    # testing delete method
    response = client.delete(
        "/seller?id=" + str(simple_seller_data["id"])
    )
    assert response.status_code == 200
