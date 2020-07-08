all = []
while True :
    x = str(input())
    if x == "q" :
        break
    else :
        x = x.split()
        all.append([x[0][:-1], int(x[1])])


all = sorted(all, key=lambda a: a[0], reverse=True)
all = sorted(all, key=lambda a: a[1], reverse=True)

for i in all[:3] :
    print(i[0] + "->" + str(i[1]))