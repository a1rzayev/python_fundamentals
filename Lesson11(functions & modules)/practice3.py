def add_item(cart, name, price, quantity=1):
    cart[name] = cart.get(name, 0) + price * quantity
    return cart

def remove_item(cart, name):
    if name in cart:
        del cart[name]
    return cart

def cart_total(cart, discount = 0):
    total = sum(cart.values())
    return total * (100 - discount) / 100

def print_cart(cart):
    for name in cart:
        print(f"{name} {cart[name]}")
    print(f"{'Total'} {cart_total(cart)}")


cart = {}

print_cart(cart)
print("\n")

add_item(cart, "Bread", 0.65, 3)
print_cart(cart)
print("\n")

add_item(cart, "Cheese", 14)
print_cart(cart)
print("\n")

add_item(cart, "Milk", 3.20, 7)
print_cart(cart)
print("\n")


remove_item(cart, "Bread")
print_cart(cart)
print("\n")

print(f"10% discount: {cart_total(cart, 10)}")


