def sort_1(x):
    return (x[1], -x[0])
def sort_2(x) :
    return (x[1], x[0])

n = int(input())
x = str(input()).split(" ")
ans = []

for i in range(n) :
    ans.append([i + 1])
    ans[i].append(int(x[i]))

ans1 = max(ans, key = sort_1)
print(ans1[0], ans1[1])
ans2 = min(ans, key = sort_2)
print(ans2[0], ans2[1])