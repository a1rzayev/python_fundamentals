is_vip = True
is_banned = False
cart_total = 101
price = 1000
discount = price*0.9
if (cart_total > 100 or is_vip) and not(is_banned):
    price = discount
    print("Your price is discounted to", price)
else :
    price = price
    print("Your price is", price)