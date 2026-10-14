# chain starts at "if" and ends at "else"

# variant1 = variant2

# variant3 has a problem with chains,
# so it print all true statements, not only the first one

age = int(input("enter your age: "))


#variant 1
if(age >= 18):
  print("you can pass exam for any vehichle DL")
elif(age >= 16):
  print("you can pass exam for only motos vehichle DL")
elif(age >= 0):
  print("you cant pass exam for any vehichle DL")
else:
  print("input correct data")
  
  
#variant 2
if(age >= 18):
  print("you can pass exam for any vehichle DL")
else:
  if(age >= 16):
    print("you can pass exam for only motos vehichle DL")
  else:
    if(age >= 0):
      print("you cant pass exam for any vehichle DL")
    else:
      print("input correct data")


#variant 3
if(age >= 18):
  print("you can pass exam for any vehichle DL")
if(age >= 16):
  print("you can pass exam for only motos vehichle DL")
if(age >= 0):
  print("you cant pass exam for any vehichle DL")
else:
  print("input correct data")
