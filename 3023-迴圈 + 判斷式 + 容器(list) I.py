list1 = []
ans = 0
while True :
    x = int(input())
    if x == -1 :
        break
    else :
        list1.append(x)
        if x > 30 :
            ans += x

list2 = sorted(list1)

print(list1)
print(list2)
print(ans)