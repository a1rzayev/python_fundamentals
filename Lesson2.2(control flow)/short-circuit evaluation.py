# gives us last element of evaluation
# "and" - evaluation stops on False
# "or" - evaluation stops on True
print("Cat" or "Dog")
print("" or "Dog")
print("" or 0 or 1 or "Dog")

print("Cat" and 0 and "Dog")

print("" or 0 or 0.0 or [])
print("123" and 1 and 0.1 and [1, 2, 3])

print(True or False)


x = 0
safe_result = (x != 0) and (10 / x > 2)
print(safe_result)