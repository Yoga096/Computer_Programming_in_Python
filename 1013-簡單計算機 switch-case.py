x = float(input())
y = float(input())
a = str(input())
ans = ("%.2f " %x) + a + (" %.2f " %y) + "="

if a == "+" :
    print(ans, "%.2f" %(x + y))
elif a == "-" :
    print(ans, "%.2f" %(x - y))
elif a == "*" :
    print(ans, "%.2f" %(x * y))
elif a == "/":
    print(ans, "%.2f" %(x / y))
