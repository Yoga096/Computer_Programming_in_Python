nk = str(input()).split(" ")
n = int(nk[0])
k = int(nk[1])
xn = str(input()).split(" ")
x = []
ans = 0

for i in xn :
    if str.isdigit(i) == True :
        x.append(int(i))

for i in x :
    while i >= k :
        ans += k
        i -= k 

print(ans)

