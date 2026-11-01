def check_age(age):
    if(age < 0):
        return "invalid age"
    elif(age >= 18):
        return "adult"
    return "child"

print(check_age(19))
print(check_age(-1))
print(check_age(15))
