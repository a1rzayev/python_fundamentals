b = input("enter any word: ")
a = b.lower()
if a == a[::-1]:
    print("palindrome")
else:
    print("not palindrome")