def check_adult(func):
    def wrapper(self):
        if self.age >= 18:
            print("License Approved!")
            return func(self)
        else:
            print("License Denied: Must be 18 or older.")
    return wrapper


class DriverSystem:
    def __init__(self, age):
        self.age = age

    def generate_numbers(self):
        for i in range(1, 51):
            yield i

    @check_adult
    def get_even_squares(self):
        squares = []
        for num in self.generate_numbers():
            if num % 2 == 0:
                squares.append(num * num)
        print(squares)



user1 = DriverSystem(15)
user1.get_even_squares()

user2 = DriverSystem(20)
user2.get_even_squares()