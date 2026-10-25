a = list(map(int, input("enter scores (x y z .....): ").split()))
for i in range(0, len(a)):
    print(f"{i+1}) {a[i]}")

print("+".join(map(str, a)), "=", sum(a)/len(a))
 