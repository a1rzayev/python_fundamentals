import math # imports library for math

print(math.pi)


age = 16

print(f"PI: {math.pi:.2f}") # count of digits after dot
print(f"PI: {math.pi:.0f}") # count of digits after dot

print(f"GPA: {14.8 / 20 :.2%}") # percentage

print("GPA: {:.2%}".format(14.8 / 20)) # percentage with format()

print(f"Salary: {1548923:,}") # separating thousands by comma

print(f"ID {age:09}") # filling zeros until you have 9 digits
