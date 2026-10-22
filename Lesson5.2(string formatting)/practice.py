a = list(map(int, input("enter numbers (x y z .....): ").split()))

print(" + ".join(map(str, a)), "=", sum(a))