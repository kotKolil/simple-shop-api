import sys

sys.path.append("..")

from fastapi.testclient import TestClient
from main import *

client = TestClient(app)

global sample_seller_data

sample_seller_data = {
    "Name": "sample Seller"
}


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_CreateMethodSellerAPIRouter():
    global sample_seller_data
    # creating test Seller
    response = client.post(
        "/Seller/",
        json={
            "name": sample_seller_data["Name"]
        },
    )
    sample_seller_data = response.json()
    assert response.status_code == 200


def test_AllMethodSellerAPIRouter():
    # getting all sellers from DB
    response = client.get(
        "/Seller/all",
    )
    assert response.status_code == 200


def test_GetMethodSellerAPIRouter():
    print(sample_seller_data)
    # testing data acess via id
    response = client.get(f"/Seller/?id={sample_seller_data["id"]}")
    assert response.json()["Name"] == sample_seller_data["Name"]
    assert response.json()["id"] == sample_seller_data["id"]


def test_PatchMethodSellerAPIRouter():
    print(sample_seller_data)
    # testing editing data in DB via api
    response = client.patch(
        "/Seller",
        json={
            "id": sample_seller_data['id'],
            "name": "sample Seller 2"
        }
    )
    assert response.status_code == 200
    sample_seller_data["Name"] = "sample Seller 2"


def test_DeleteMethodAPIRouter():
    print(sample_seller_data)
    # testing delete method
    response = client.delete(
        "/Seller?id=" + str(sample_seller_data["id"])
    )
    assert response.status_code == 200
