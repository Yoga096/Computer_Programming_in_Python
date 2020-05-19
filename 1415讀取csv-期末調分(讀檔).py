import math

s = open("./" + str(input())).readlines()
ans = []
for i in s[1:] :
    if math.sqrt(int(i.split(",")[1][:-1])) * 11 < 60 :
        ans.append(int(i.split(",")[0]))
for i in sorted(ans)[:-1] :
    print(i, end = " ")
print(sorted(ans)[-1])