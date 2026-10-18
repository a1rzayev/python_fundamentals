import random # library for generating random numbers

suspect_found = False
while(not suspect_found):
    i = random.randint(1, 10) # random number from 1 to 11
    if(i == 7):
        suspect_found = True
        print("we found suspect! breaking the party")
        break
    print(i)