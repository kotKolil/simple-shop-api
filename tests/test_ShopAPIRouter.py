import sys
sys.path.append("..")
from main import *
from fastapi.testclient import TestClient

client = TestClient(app)

global sample_seller_data
global sample_shop_data

sample_seller_data = {
    "name": "sample seller",
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
        '/seller/',
        json = sample_seller_data
    )
    sample_seller_data = response.json()
    sample_shop_data["SellerId"] = sample_seller_data["id"]
    response = client.post(
        "/shop/",
        json = sample_shop_data
    )
    sample_shop_data = response.json()
    assert response.status_code == 200

def test_AllMethodAPI():
    global sample_seller_data
    global sample_shop_data
    response = client.get("/shop/all/")
    assert response.status_code == 200

def test_GETMethodTest():
    print(sample_shop_data)
    response = client.get(f"/shop?id={sample_shop_data['id']}")
    print(response.json())
    assert response.json()['name'] == sample_shop_data["name"]
    assert response.json()["id"] == sample_shop_data["id"]

def test_PATCHMethodTest():
    sample_shop_data["name"] = "another sample shop"
    sample_shop_data["address"] = "another sample address"
    response = client.patch(
        url = "/shop",
        json = sample_shop_data
    )
    assert response.status_code == 200

def test_DELETEMethodTest():
    #deleting shop
    response = client.delete(f"/shop?id={sample_shop_data['id']}")
    #deleting seller
    response2 = client.delete(f"/seller?id={sample_seller_data["id"]}")
    assert response.status_code == 200