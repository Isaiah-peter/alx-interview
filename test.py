#!/usr/bin/python3
import random
import json

colors = [{"id": 1, "name": "red"},    {"id": 2, "name": "green"},    {"id": 3, "name": "blue"},    {"id": 4, "name": "yellow"},    {"id": 5, "name": "purple"},    {
    "id": 6, "name": "orange"},    {"id": 7, "name": "pink"},    {"id": 8, "name": "brown"},    {"id": 9, "name": "gray"},    {"id": 10, "name": "black"}]

sizes = [{"id": 1, "name": "XS"},    {"id": 2, "name": "S"},    {"id": 3, "name": "M"},    {"id": 4, "name": "L"},    {"id": 5, "name": "XL"},    {
    "id": 6, "name": "XXL"},    {"id": 7, "name": "XXXL"},    {"id": 8, "name": "4XL"},    {"id": 9, "name": "5XL"},    {"id": 10, "name": "6XL"}]

products = []


for i in range(10):
    product = {
        "id": i + 1,
        "img": f"https://images.pexels.com/photos/{random.randint(1000000, 9999999)}/pexels-photo-{random.randint(1000000, 9999999)}.jpeg",
        "description": "good product",
        "price": random.randint(100, 500),
        "Color": random.sample(colors, k=random.randint(1, len(colors))),
        "Size": random.sample(sizes, k=random.randint(1, len(sizes)))
    }
    products.append(product)

    with open("data.json", "w") as w:
        w.write(json.dumps(product))


json_products = json.dumps(products)

print(json_products)