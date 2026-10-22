answer = input("yes or no? ")
if answer.strip().lower() == "yes":
    print("okay, thanks for agreement")
elif answer.strip().lower() == "no":
    print("okay, thanks for declining")
else:
    print("wrong option")