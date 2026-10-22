text = "       Hello my name is Asif!        "

print(text.upper())
print(text.lower())

print(text.title()) # every words' first letter is upper
print(text.capitalize()) # only first word's first letter is upper


print("|" + text.strip() + "|")
print("|" + text.lstrip() + "|") # l - left
print("|" + text.rstrip() + "|") # r - right
