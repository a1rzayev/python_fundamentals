age = 16
print(age > 16)
print(age == 21)

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # True, checking data
print(a is b) # False, different variables(different memory location)

str1 = "123"
str2 = "123"
print(str1 == str2) # True, checking data
print(str1 is str2) # True, same variable(same memory location) because of string interning