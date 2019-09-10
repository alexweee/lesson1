def discounted(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 100:
        price_with_discount = price

    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount

p = discounted(100, 101)
print(p)

