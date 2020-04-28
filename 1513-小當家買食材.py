n = int(input())
dict = {}
for i in range(n) :
    x = str(input()).split(" ")
    if x[0] in dict :
        dict[x[0]] += int(x[1])
    else :
        dict[x[0]] = int(x[1])

ans = max(dict, key=dict.get)
print(ans, dict[ans])