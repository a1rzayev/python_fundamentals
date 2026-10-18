numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = -1
while(i < 9):
    i += 1
    print("i =", i)
    if(numbers[i] == 7):
        suspect_found = True
        print("we found suspect! breaking the party")
        continue
    print(numbers[i])