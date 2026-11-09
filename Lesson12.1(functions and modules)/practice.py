def travel(type):
    return type()

def drive():
    return "car"

def train():
    return "train"

def fly():
    return "plane"

distance = int(input("Distance: "))

if(distance < 200):
    print("travel with:", travel(drive))
elif(distance < 2000):
    print("travel with:", travel(train))
elif(distance >= 2000):
    print("travel with:", travel(fly))