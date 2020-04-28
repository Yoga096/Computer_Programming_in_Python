n = int(input())
A = input().split(" ")
a = []

for i in A :
    if str.isdigit(i) == True :
        a.append(int(i))
#for i in a :
#    print(i)
if n % 2 == 0 :
    x = int(n / 2)
    ans = (a[x-1] + a[x]) / 2
    if ans % 1 == 0 :
        print(int(ans))
    else :
        ans = (a[x-1] + a[x] + 1) / 2
        print(int(ans))
else :
    x = int((n + 1) / 2)
    ans = a[x - 1]
    print(ans)
