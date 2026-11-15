class BankAccount:
    def __init__(self, owner, balance, *args):
        self.owner = owner
        self.balance = balance
        self.add_info = args

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}$")

    def withdraw(self, amount):
        if(self.balance < amount):
            print("Not enough funds")
            return 0
        self.balance -= amount
        print(f"Withdrawed: {amount}$")

    def display_balance(self):
        print(f"BALANCE: {self.balance}$")