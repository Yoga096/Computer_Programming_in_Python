n = int(input())
a1 = 0
a2 = 0
a3 = 0

for i in range(n) :
    x = str(input())
    if x.islower() == True :
        a1 += 1
    elif x.isupper() == True :
        a2 += 1
    else :
        a3 += 1

print(a1, a2, a3)