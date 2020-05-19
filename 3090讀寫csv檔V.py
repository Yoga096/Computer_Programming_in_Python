m = open("math_list.csv", encoding = "big5").readlines()
e = open("english_list.csv", encoding = "big5").readlines()
ms = []
es = []
a = [[], [], [], [], []]

for i in m[1:] :
    i = i.split(",")[0]
    if i in ms :
        pass
    else :
        ms.append(i)
        a[1].append(i)
        a[2].append(i)
        a[4].append(i)

for i in e[1:] :
    i = i.split(",")[0]
    if i in es :
        pass
    else :
        es.append(i)
        if i in ms :
            a[0].append(i)
            a[1].remove(i)
            a[2].remove(i)
        else :
            a[1].append(i)
            a[3].append(i)
            a[4].append(i)

for i in a :
    print(sorted(i))

print(sorted(list(set(ms) - set(es))))