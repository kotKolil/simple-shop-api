import sys

sys.path.append("..")

from fastapi.testclient import TestClient
from main import *

client = TestClient(app)

global sample_seller_data

sample_seller_data = {
    "Name": "sample seller"
}


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_CreateMethodSellerAPIRouter():
    global sample_seller_data
    # creating test seller
    response = client.post(
        "/seller/",
        json={
            "name": sample_seller_data["Name"]
        },
    )
    sample_seller_data = response.json()
    assert response.status_code == 200



def test_AllMethodSellerAPIRouter():
    # getting all sellers from DB
    response = client.get(
        "/seller/all",
    )
    assert response.status_code == 200

def test_GetMethodSellerAPIRouter():
    print(sample_seller_data)
    # testing data acess via id
    response = client.get(f"/seller/?id={sample_seller_data["id"]}")
    assert response.json()["Name"] == sample_seller_data["Name"]
    assert response.json()["id"] == sample_seller_data["id"]


def test_PatchMethodSellerAPIRouter():
    print(sample_seller_data)
    # testing editing data in DB via api
    response = client.patch(
        "/seller",
        json={
            "id": sample_seller_data['id'],
            "name": "sample seller 2"
        }
    )
    assert response.status_code == 200
    sample_seller_data["Name"] = "sample seller 2"


def test_DeleteMethodAPIRouter():
    print(sample_seller_data)
    # testing delete method
    response = client.delete(
        "/seller?id=" + str(sample_seller_data["id"])
    )
    assert response.status_code == 200
