m = int(input())
a = str(input()).split(",")
b = str(input()).split(",")

x1 = int(a[0])
y1 = int(a[1])
x2 = int(b[0])
y2 = int(b[1])

for i in range(m) :
    line = ""
    for j in range(m) :
        if (i+1 == x1) & (j+1 == y1) :
            line += "0 "
        elif (i+1 == x2) & (j+1 == y2) :
            line += "x "
        else :
            line += "- "

    print(line)
            
        