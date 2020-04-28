x = []
while True :
    a = str(input())
    if a == "-1" :
        break
    else :
        x.append(int(a))
x.reverse()
for i in x :
    print(i)
    for j in range(i) :
        print()

print("-" * 20)