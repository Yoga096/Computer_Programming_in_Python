n = int(input())
y = 1
for i in range(1, n+1) :
    x = []
    for j in range(1, i+1) :
        x.append(y)
        y += 1
    for a in x :
        print(a, end = " ")
    print()

