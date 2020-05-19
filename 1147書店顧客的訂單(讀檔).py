f0 = open("./" + str(input()), mode = 'r').readlines()
dic = {}
for x in f0 :
    i = x.split(",")
    i0 = i[0].lower()
    if i0 in dic.keys() :
        dic[i0] += int(i[1])
    else :
        dic[i0] = int(i[1])

for i in sorted(dic) :
    print(i + "," + str(dic[i]))