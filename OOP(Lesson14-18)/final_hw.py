class CreditCard:
  def pay(self, amount):
    print(f"Paid ${amount:.2f} using Credit Card.")


class PayPal:
  def pay(self, amount):
    print(f"Paid ${amount:.2f} via PayPal.")


class Cash:
  def pay(self, amount):
    print(f"Paid ${amount:.2f} in Cash.")


payments = [CreditCard(), PayPal(), Cash()]

for payment in payments:
  payment.pay(50)