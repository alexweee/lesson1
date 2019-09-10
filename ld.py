phones = ["apple", "samsung", "xiaomi"]

product = {
    "name": "iPhone Xs", 
    "stock": 5, 
    "price": 65000.0,
    "recomend": phones,
}


print(product["recomend"])

print(product["recomend"][1])

product["recomend"].append("iPhone 6")

print(product)