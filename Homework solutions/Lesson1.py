username = (input("enter your username: "))
age = int(input("enter your age: "))
scores = list(map(float, input("enter your scores: ").split()))

avg_score = (sum(scores)).__round__(2)
Pro_status = input("enter your status[y/n]: ")

if Pro_status.lower() == "y": 
    Pro_status = True
elif Pro_status.lower() == "n":
    Pro_status = False
else:
    print("error: invalid input for status, please enter 'y' or 'n'")
    
print("Gamer: ", username)
print("age: ", age)
print("scores history: ", end="")
print(scores, sep="-")
print("avg score:", avg_score)
print("Your status is", Pro_status)