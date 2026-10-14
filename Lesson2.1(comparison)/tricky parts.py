age = 20
criminal_records = []
schools = ["university", "academy"]
workplaces = ["f5 llc", "step it"]

can_apply = (bool(criminal_records) != True) and ((bool(schools) == True) or (bool(workplaces) == True))

can_apply = False

print(can_apply is False)


has_driverslicense = False

print(has_driverslicense is True)

