def discounted(price, discount):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
    except ValueError:
        print("пожалуйста введите только цифры")
    if discount >= 100:
        price_with_discount = price

    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount

p = discounted("рав", 101)
print(p)

