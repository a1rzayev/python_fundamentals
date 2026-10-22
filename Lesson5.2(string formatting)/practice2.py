import math

a = int(input("Enter the radius of the wheel: "))
area = math.pi * a**2
print(area.__round__(2))