import sys

sys.path.append("..")
from main import *
from fastapi.testclient import TestClient

client = TestClient(app)

global sample_seller_data
global sample_shop_data

sample_seller_data = {
    "name": "sample Seller",
    "id": ""
}
sample_shop_data = {
    "name": "Sample Shop",
    "address": "Sample Address"
}


def test_CreateMethodAPI():
    global sample_seller_data
    global sample_shop_data
    response = client.post(
        '/Seller/',
        json=sample_seller_data
    )
    sample_seller_data = response.json()
    sample_shop_data["SellerId"] = sample_seller_data["id"]
    response = client.post(
        "/Shop/",
        json=sample_shop_data
    )
    sample_shop_data = response.json()
    assert response.status_code == 200


def test_AllMethodAPI():
    global sample_seller_data
    global sample_shop_data
    response = client.get("/Shop/all/")
    assert response.status_code == 200


def test_GETMethodTest():
    print(sample_shop_data)
    response = client.get(f"/Shop?id={sample_shop_data['id']}")
    print(response.json())
    assert response.json()['name'] == sample_shop_data["name"]
    assert response.json()["id"] == sample_shop_data["id"]


def test_PATCHMethodTest():
    sample_shop_data["name"] = "another sample Shop"
    sample_shop_data["address"] = "another sample address"
    response = client.patch(
        url="/Shop",
        json=sample_shop_data
    )
    assert response.status_code == 200


def test_DELETEMethodTest():
    #deleting Shop
    response = client.delete(f"/Shop?id={sample_shop_data['id']}")
    #deleting Seller
    client.delete(f"/Seller?id={sample_seller_data["id"]}")
    assert response.status_code == 200