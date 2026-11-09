def age_check(x):
    if x < 0:
        raise ValueError("Age cant be negative!")
    
try:
    age = int(input("enter your age:"))
    age_check(age)

except ValueError as err:
    print(err)

else:
    print("your age:", age)