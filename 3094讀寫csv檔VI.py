s = open("../app/score.csv").readlines()
a = [[], [], []]
for i in sorted(s[1:]) :
    i = i.split(",")
    if int(i[1]) >= 60 :
        a[0].append(i[0])
        if int(i[2][:-1]) < 60 :
            a[2].append(i[0])
    if int(i[2][:-1]) >= 60 :
        a[1].append(i[0])
print(a[0], a[1], a[2], len(s)-1, sep = "\n")