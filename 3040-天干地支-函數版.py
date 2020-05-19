def YEAR(list) :
    for i in list :
        a1 = (i-3) % 10 -1
        a2 = (i-3) % 12 -1
        ans.append(str(i) + " = " + x1[a1] + x2[a2] + "年")
    return(ans)

x1 = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
x2 = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']

ylist = []
ans = []

while True :
    x = str(input())
    if x == "q" :
        break
    else :
        ylist.append(int(x))

for i in YEAR(ylist) :
    print(i)