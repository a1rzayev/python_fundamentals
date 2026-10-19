# mutable - changable
# immutable - unchangable

# print('hello ' * 5) # prints hello 5 times

name = "Muradxan"

print(len(name))
print("First:", name[0], end=" | ") # END - by default "\n"(new line), but we can change
print("Last:", name[-1])

print(name)

# name[0] = "m" WE CANT CHANGE STRING!!!

name = "m" + name[1:] # but can create new one
print(name)


str1 = 'Hello'
# doesnt matter which quotes do you use
str2 = "Hello"

print("""My name is Asif
    I am a programming instructor
    etc.....
    jksdhfkjasdhf
    asdhfjkahskdjfh
    asdhfjkasdhf""") #prints exactly the same as you wrote

