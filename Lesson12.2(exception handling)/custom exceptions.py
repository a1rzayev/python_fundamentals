class InsufficientBalanceException(Exception):
    pass # doing nothing

def withdraw(balance, amount):
    if(amount > balance):
        raise InsufficientBalanceException("not enough funds!")
    return balance - amount

try:
    print(withdraw(100, 130))

except InsufficientBalanceException as IBE:
    print(IBE)

x = 5.0

if(type(x) != type(0.0)):
    print("not float")