all = []
n = int(input())
for i in range(n) :
    all.append([str(input()), int(input()), int(input())])
m = int(input())

if m != 0 :
    all = sorted(all, key=lambda x:x[m-1])

for i in all :
    print("Name:", i[0] + "\nLv:", str(i[1]) + "\nHP:", str(i[2]) + "\n")

