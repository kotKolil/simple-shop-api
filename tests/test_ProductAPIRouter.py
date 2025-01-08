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
    global sample_product_data, sample_shop_data, sample_seller_data

    #creating sample seller
    response = client.post(
        url='/seller/',
        json = sample_seller_data
    )
    sample_seller_data = response.json()
    print(sample_seller_data)
    sample_shop_data["SellerId"] = sample_seller_data["id"]
    #creating sample shop
    response = client.post(
        url= "/shop/",
        json = sample_shop_data
    )
    #creating sample product
    sample_shop_data = response.json()
    sample_product_data["ShopId"] = sample_shop_data["id"]
    response = client.post(
        url= "/product",
        json = sample_product_data
    )
    sample_product_data = response.json()

    assert response.status_code == 200

def test_AllMethodTest():
    global sample_product_data
    response = client.get("/product/all")
    assert response.status_code == 200


def test_GETMethodTest():
    print(sample_product_data)
    response = client.get(f"/product?id={sample_product_data['id']}")
    assert response.status_code == 200
    assert response.json()== sample_product_data

def test_PATCHMethodTest():
    sample_product_data["name"] = "another sample product"
    sample_product_data["price"] = 666
    response = client.patch(
        "/product",
        json = sample_product_data
    )
    assert response.status_code == 200

def test_DELETEMethod():
    print(sample_product_data)
    response = client.delete(f"/shop?id={sample_product_data['id']}")
    client.delete(f"/seller?id={sample_shop_data['id']}")
    client.delete(f"/seller?id={sample_seller_data['id']}")
    assert response.status_code == 200