def sum_of_digits(n):
    if(n < 10):
        return n
    return n % 10 + sum_of_digits(n // 10)
    

# 1234 = 4 + 3 + 2 + 1

# [0-9], 7 = 7 