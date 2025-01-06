import sys
sys.path.append("...")
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

#creating sample seller for shop
response = client.post(
    "/seller/",
    json={
        "name": sample_seller_data["name"]
    },
)
#getting user id for sample shop
response = client.get('/seller/all')
for i in response.json():
    print(response.json())
    if i["Name"] == sample_seller_data["name"]:
        sample_seller_data["id"] = i["id"]
        sample_shop_data["SellerId"] = i['id']

def test_CreateMethodAPI():
    response = client.post(
        "/shop/",
        json = sample_shop_data
    )
    assert response.status_code == 201

def test_AllMethodAPI():
    global sample_seller_data
    global sample_shop_data
    response = client.get("/shop/all/")
    assert response.status_code == 200
    for i in response.json():
        if i["Name"] == sample_shop_data["name"]:
            sample_shop_data["id"] = i["id"]

def test_GETMethodTest():
    print(sample_shop_data)
    response = client.get(f"/shop?id={sample_shop_data['id']}")
    assert response.json()['Name'] == sample_shop_data["name"]
    assert response.json()["id"] == sample_shop_data["id"]

def test_PATCHMethodTest():
    sample_shop_data["SellerId"] = sample_seller_data["name"]
    sample_shop_data["name"] = "another sample shop"
    sample_shop_data["address"] = "another sample address"
    response = client.patch(
        url = "/shop",
        json = sample_shop_data
    )
    assert response.status_code == 200

def test_DELETEMethodTest():
    print(sample_shop_data)
    response = client.delete(f"/shop?id={sample_shop_data['id']}")
    assert response.status_code == 200