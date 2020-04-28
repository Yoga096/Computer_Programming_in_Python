x = str(input())[::-1].split(";")
ans = ""
for i in range(len(x)-1) :
    print(x[i], end = " ")
print(x[-1])

