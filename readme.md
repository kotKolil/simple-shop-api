[TOC]



# Simple Shop API

This is open-source project, that shows functionality of Fast API and SQL Alchemy in simple API

## structure of project:



![strurcture](assets\strurcture.PNG)

### Models -

In this folder defined classes, implementing tables in database

### Routers

In this folder placed classes, that provide API to tables in database

### Tests

In this folder placed tests, that check work of app and API

### .gitignore

in this classes defined names of files. that doesen't must be in git repo

### licence.txt

defining rules of code modification and usage

### r.txt

defined list of libraries, that app is using in it work

### readme.md

provide documentation about project

# API entrypoints

In this topic described API entrypoints in app and how they use in table

| URL              | METHOD | DESCRIPTION                          | JSON FORMAT INPUT                                       | JSON FORMAT OUTPUT                             |
|------------------|--------|--------------------------------------|--------------------------------------------------------|------------------------------------------------|
| `/seller`        | POST   | Create a new seller (user).         | `{ "name": "string" }`                                | `{ "id": integer, "Name": "string" }`        |
| `/seller`        | GET    | Retrieve seller details by ID.      | `{ "id": integer }` (query parameter)                 | `{ "id": integer, "Name": "string" }`        |
| `/seller/all`    | GET    | Retrieve all sellers.                | N/A                                                    | `[ { "id": integer, "Name": "string" }, ... ]` |
| `/seller`        | PATCH  | Update seller information.           | `{ "id": integer, "name": "string" }`                 | `HTTP 200 OK`                                  |
| `/seller`        | DELETE | Delete a seller by ID.              | `{ "id": integer }` (query parameter)                 | `HTTP 200 OK`                                  |
| `/shop`          | POST   | Create a new shop.                  | `{ "SellerId": integer, "name": "string", "address": "string" }` | `{ "id": integer, "SellerId": integer, "name": "string", "address": "string" }` |
| `/shop`          | GET    | Retrieve shop details by ID.        | `{ "id": integer }` (query parameter)                 | `{ "id": integer, "SellerId": integer, "name": "string", "address": "string" }` |
| `/shop/all`      | GET    | Retrieve all shops.                  | N/A                                                    | `[ { "id": integer, "SellerId": integer, "name": "string", "address": "string" }, ... ]` |
| `/shop`          | PATCH  | Update shop information.             | `{ "id": integer, "SellerId": integer, "name": "string", "address": "string" }` | `HTTP 200 OK`                                  |
| `/shop`          | DELETE | Delete a shop by ID.                | `{ "id": integer }` (query parameter)                 | `HTTP 200 OK`      |
| `/product`         | POST   | Create a new product.                | `{ "name": "string", "ShopId": integer, "price": number }` | `{ "id": integer, "shopId": integer, "name": "string", "price": number }` |
| `/product`         | GET    | Retrieve product details by ID.      | `{ "id": integer }` (query parameter)                 | `{ "id": integer, "shopId": integer, "name": "string", "price": number }` |
| `/product/all`     | GET    | Retrieve all products.               | N/A                                                    | `[ { "id": integer, "shopId": integer, "name": "string", "price": number }, ... ]` |
| `/product`         | PATCH  | Update product information.          | `{ "id": integer, "name": "string", "ShopId": integer, "price": number }` | `HTTP 200 OK`                                  |
| `/product`         | DELETE | Delete a product by ID.              | `{ "id": integer }` (query parameter)                 | `HTTP 200 OK`                                  |

# How to test app

to test app, you need to do this steps:
1.)install libraries from r.txt

2.) go to directories "tests"

3.) write in console "pytest" and run

Congratulations, you are tested the app!

# How to start app

1.)install libaries from r.txt

2.) go to root dir of project

3.) write "uvicorn main:app" and run

Congratulations, you are started the app!