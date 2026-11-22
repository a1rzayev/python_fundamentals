class Vehicle:
    def __init__(self, brand:str, model:str, rental_price:float):
        self.brand = brand
        self.model = model
        self.rental_price = rental_price
        self.__available = True

    @property
    def available(self):
        return self.__available

    def rent(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_vehicle(self):
        self.__available = True

    def calculate_rent(self, days):
        return self.rental_price * days

    def display_info(self):
        return f"{self.brand} {self.model} - ${self.rental_price}/day (Available: {self.__available})"


class Car(Vehicle):
    def display_info(self):
        return f"Car: {self.brand} {self.model} - ${self.rental_price}/day (Available: {self.available})"


class Moto(Vehicle):
    def __init__(self, brand, model, rental_price, hourly_rate):
        super().__init__(brand, model, rental_price)
        self.hourly_rate = hourly_rate

    def display_info(self):
        return f"Moto: {self.brand} {self.model} - ${self.hourly_rate}/hr (Available: {self.available})"

    def calculate_rent(self, days, hours=None):
        if hours is not None:
            return self.hourly_rate * hours
        return self.hourly_rate * days * 24


c = Car("Toyota", "Corolla", 50)
m = Moto("Honda", "CB500", 35, 5)
print(c.display_info(), c.calculate_rent(2))
print(m.display_info(), m.calculate_rent(2), m.calculate_rent(0, hours=4))