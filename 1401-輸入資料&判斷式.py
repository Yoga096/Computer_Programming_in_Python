i = 1
f = 1.0
while True :
    x = str(input())
    if x == "q" :
        break    
    elif float(x) % 1 == 0 :
        i *= int(x)
    else :
        f *= float(x)
        
print("%.2f" %f)
print(i)
if f > float(i) :
    print("Float > Int")
elif f == float(i) :
    print("Float = Int")
else :
    print("Float < Int")

