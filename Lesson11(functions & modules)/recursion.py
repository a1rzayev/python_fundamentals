
def factorial(n:int):
    if(n <= 1):
        return 1
    return n * factorial(n - 1)

# 4 * factorial(3)
# 4 * 3 * factorial(2)
# 4 * 3 * 2 * factorial(1)
# 4 * 3 * 2 * 1

# factorial 4! = 4 * 3 * 2 * 1 

# 4 * (3 * (2 * (1)))

# n = 4
# return 4 * factorial(4-1)

# n = 3
# return 3 * factorial(3-1)

# n = 2
# return 2 * factorial(2-1)

# n = 1
# return 1 * factorial(1-1)