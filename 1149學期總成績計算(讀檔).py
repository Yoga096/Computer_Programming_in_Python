def avg(x, avg0 = 0) :
    for i in x[1:5] :
        avg0 += int(i)
    avg0 *= 0.7 / 4
    avg0 += int(x[5][:-1]) * 0.75
    if (avg0 >= 60) | (x[5] != "40\n") :
        return avg0
    else :
        return 60.0

s = open("./" + str(input())).readlines()
for i in s[1:] :
    i = i.split(",")
    print(i[0], "%.2f" %avg(i))