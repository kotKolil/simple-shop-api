import sys
sys.path.append("..")

from main import *
from fastapi.testclient import TestClient

global sample_product_data, sample_shop_data, sample_seller_data

client = TestClient(app)

sample_product_data = {
    "name": "sample product",
    "price": 777
}

sample_seller_data = {
    "name": "sample seller"
}
sample_shop_data = {
    "name": "Sample Shop",
    "address": "Sample Address"
}



def test_CreateMethodTest():

    #creating sample seller for shop
    response = client.post(
        "/shop/",
        json={
            "name": sample_seller_data["name"]
        },
    )
    #getting shop id for sample shop
    response = client.get('/shop/all')
    for i in response.json():
        if i["Name"] == sample_seller_data["name"]:
            sample_seller_data["id"] = i["Id"]
            sample_shop_data["SellerId"] = i['Id']

    response = client.get("/shop/all")
    for i in response.json():
        if i["Name"] == sample_shop_data["name"]:
            sample_shop_data["id"] = i["id"]
            sample_product_data["id"] = i["id"]

    response = client.post(
        "/product",
        json= sample_product_data
    )

    assert response.status_code == 201

def test_AllMethodTest():
    global sample_product_data
    response = client.get("/product/all")
    assert response.status_code == 200

    for i in response.json():
        if i["name"] == sample_shop_data["name"]:
            sample_product_data["id"] = i["Id"]

def test_GETMethodTest():
    print(sample_product_data)
    response = client.get(f"/product?id={sample_product_data['id']}")
    assert response.status_code == 200
    assert response.json()['Name'] == sample_product_data["name"]
    assert response.json()["Addess"] == sample_product_data["address"]
#
# def test_PATCHMethodTest():
#     sample_product_data["name"] = "another sample product"
#     sample_product_data["price"] = 666
#     response = client.patch(
#         "/product",
#         json = sample_product_data
#     )
#     assert response.status_code == 201
#
# def test_DELETEMethod():
#     response = client.delete(f"/shop?id={sample_product_data['id']}")
#     assert response.status_code == 200