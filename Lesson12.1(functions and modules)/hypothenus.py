a = float(input("input a:"))
b = float(input("input b:"))

hypothenus = lambda a, b: (a*a + b*b) ** 0.5

def hyphotenus_func(a, b):
    return (a*a + b*b) ** 0.5

print(hypothenus(a, b))
print(hyphotenus_func(a, b))

