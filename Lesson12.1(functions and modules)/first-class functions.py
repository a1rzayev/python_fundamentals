def shout(text):
    return text.upper() + "!"

text = "salam"

print(shout("hello"))
print(shout)
print(type(shout))
print(type(text))

yell = shout
print(yell("ada"))
print(yell)
print(shout("ada"))
