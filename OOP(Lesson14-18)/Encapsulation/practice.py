class Temperature:
    def __init__(self, celsius = 0):
        if celsius < -273.15:
            raise ValueError("Cannot be below -273.15 C")
        self.__celsius = celsius

    @property
    def celcius(self):
        return self.__celsius

    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32
    
    @property
    def kelvin(self):
        return (self.__celsius + 273.15)
    
temp = Temperature(9)

print(f"{temp.celcius} C")
print(f"{temp.fahrenheit} F")
print(f"{temp.kelvin} K")