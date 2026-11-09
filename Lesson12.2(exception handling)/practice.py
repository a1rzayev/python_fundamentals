def check_balance(balance, amount):
    if type(balance) != float and type(amount) != float or int:
        raise TypeError("balance and amount must be float")
    if balance < amount:
        raise ValueError("balannce less than amount")

def withdraw(balance, amount):
    check_balance(balance, amount)
    balance -= amount
    return balance

def deposit(balance, amount):
    check_balance(balance, amount)
    balance += amount
    return balance


balance = float(input("enter balance: "))
amount = float(input("enter amount: "))

check_balance(balance, amount)