name = input("Enter your name: ")
print("Hello, " + name + "!")

age = int(input("Enter your age: "))
print(age + 1)

x, y = map(int, input("Input X and Y: ").split()) # split() splits the input string into a list of strings, and map(int, ...) converts each string to an integer
print("X + Y =", x + y)

numbers = list(map(int, input("Input numbers: ").split()))

print("Numbers:", numbers)
print("Sum of numbers:", sum(numbers))



three_dimensions = list(map(int, input("Input height, length, width respectively: ").split()))

print("Height:", three_dimensions[0])
print("Length:", three_dimensions[1])
print("Width:", three_dimensions[2])

print("Volume:", three_dimensions[0] * three_dimensions[1] * three_dimensions[2])
print("Area:", three_dimensions[1] * three_dimensions[2])