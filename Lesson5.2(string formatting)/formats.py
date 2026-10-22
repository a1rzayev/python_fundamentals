name = "Muradkhan"
age = 16
education = "ADA"
gpa = 3.95

print("I am", name, ". I am", age, "years old.", "I study in", education)

print("I am " + name + ". I am " + str(age) + " years old." + " I study in " + education)

print(f"I am {name}. I am {age} years old. I study in {education}")

print("I am {}. I am {} years old. I study in {}".format(name, age, education))

print("I am {0}. I am {1} years old. I will finish {2} when i turn {1}".format(name, age, education))

# %s - string, %d - digit, %f - float
print("I am %s. I am %d years old. GPA: %f" % (name, age, gpa))
