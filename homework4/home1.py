def cake_price(cake_type,  cake_size):
    cake_size = round(cake_size,2)
    totalPrice = -1
    if cake_type.lower() == "napoleon cake":
        totalPrice = cake_size * cake_size * 0.08
    elif cake_type.lower() == "chocolate cake":
        totalPrice = 3.14 * cake_size ** 2 * 0.05
    elif cake_type.lower() == "strawberry cake":
        totalPrice = 3.14 * cake_size ** 2 * 0.04
    return totalPrice

print (cake_price("napoleon cake", 10))
print (cake_price("chocolate cake", 12.5))
print (cake_price("apple pie", 5))
