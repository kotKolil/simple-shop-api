import sys

sys.path.append("..")

from main import *
from fastapi.testclient import TestClient

global sample_product_data, sample_shop_data, sample_seller_data

client = TestClient(app)

sample_product_data = {
    "name": "sample Product",
    "price": 777
}

sample_seller_data = {
    "name": "sample Seller"
}
sample_shop_data = {
    "name": "Sample Shop",
    "address": "Sample Address"
}


def test_CreateMethodTest():
    global sample_product_data, sample_shop_data, sample_seller_data

    # creating sample Seller
    response = client.post(
        url='/Seller/',
        json=sample_seller_data
    )
    sample_seller_data = response.json()
    sample_shop_data["SellerId"] = sample_seller_data["id"]
    # creating sample Shop
    response = client.post(
        url="/Shop/",
        json=sample_shop_data
    )
    # creating sample Product
    sample_shop_data = response.json()
    sample_product_data["ShopId"] = sample_shop_data["id"]
    response = client.post(
        url="/Product",
        json=sample_product_data
    )
    sample_product_data = response.json()

    assert response.status_code == 200


def test_AllMethodTest():
    global sample_product_data
    response = client.get("/Product/all")
    assert response.status_code == 200


def test_GETMethodTest():
    response = client.get(f"/Product?id={sample_product_data['id']}")
    assert response.status_code == 200
    assert response.json() == sample_product_data


def test_PATCHMethodTest():
    sample_product_data["name"] = "another sample Product"
    sample_product_data["price"] = 666
    response = client.patch(
        "/Product",
        json=sample_product_data
    )
    assert response.status_code == 200


def test_DELETEMethod():
    response = client.delete(f"/Shop?id={sample_product_data['id']}")
    client.delete(f"/Seller?id={sample_shop_data['id']}")
    client.delete(f"/Seller?id={sample_seller_data['id']}")
    assert response.status_code == 200
