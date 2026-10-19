text = "ADA University"

# ADA
print(text[0:3])
print(text[:3])
print(text[:-11])

# University
print(text[4:])
print(text[-10:]) # -10 -> end by step 1

# whole copy
print(text[::]) # if you dont mention - gets default(0 : -1 : 1)


# every second character
print(text[::2])

# whole copy(reversed)
print(text[::-1])


print(text[100]) # OutOfRange error (no index exists under 100)

print(text[100:]) # slicing never gives an error