# 1
# 3
# 5
# 7

#   *
#  ***
# *****
#*******

def draw_pyramid():
    for i in range(1, 5):
        print((" " * (4 - i)) + ("*" * (i * 2 - 1)))

draw_pyramid()