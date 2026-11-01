def avg_grade(*grades): # getting as a list
    summ = sum(grades)
    return summ / len(grades)

print(avg_grade(98, 95, 93, 92, 88, 75, 64, 90))

def avg_grade2(**grades): # getting as a dict
    summ = 0
    for elem in grades:
        summ += grades[elem]
    return summ / len(grades)

dicts = {"Muradkhan": 98, "Ziya": 95}

print(avg_grade2(**dicts))

