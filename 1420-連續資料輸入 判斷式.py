def is_float(i):
    try:
        float(i)
        return True
    except ValueError:
        pass

a1 = 0
a2 = 0
while True :
    x = str(input())
    if x == "q" :
        break
    elif is_float(x) == True :
        a1 += float(x)
        a2 += int(float(x))   

a1 -= float(a2)
a1 = "%.3f" % a1
if int(a1[-1]) >= 5 :
    a3 = float(a1[:-1]) + 0.01
else :
    a3 = float(a1[:-1])

print("%.2f" %a3)