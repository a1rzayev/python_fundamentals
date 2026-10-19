string1 = "            Testing our string              "

print(len(string1))
print(string1[0])
print(string1[1 : 10 : 2]) # start : end(not included) : step
print(string1[9 : 0 : -2]) 
 
print(string1[0])
print(string1[-1]) # starting backwards

print(string1) 
print(string1.strip()) # default: removes spaces from start and end

print(string1.split("s")) # diving some text by using keywoard(on default by spaces)
print(string1.split())

print("Age: " + str(18))

