text = "Muradkhan is studying in ADA School for last 2 years"

print(text.find("ADA")) # finds first match
print(text.find("Java")) # didnt find, result = -1
print(text.index("ADA"))
# print(text.index("Java")) # gives ValueError, if didnt find

# print(text.startswith("Murad")) # is string starting with "****"
# print(text.endswith("rs")) # is string ending with "****"


"""Our implementation of startswith"""

name = "Muradxan"

is_starting = True

for i in range(len(name)):
    if(text[i] != name[i]):
        is_starting = False
        break

print("True!!!") if is_starting else print("False!!!")



