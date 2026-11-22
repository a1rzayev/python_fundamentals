name = input("Enter your name: ")
age = int(input("Enter your age: "))

with open("users.txt", "a") as file:
    file.write(f"Name: {name}, Age: {age}\n")

print("User info added successfully")