# * - 1D list

def order_coffee(type:str, size:str, *extras):
    dict = {"type": type, "size": size, "extras": extras}
    return dict

print(order_coffee("Americano", "Medium"))
print(order_coffee("Americano", "Medium", "sugar", "caramel", "dark sugar"))

