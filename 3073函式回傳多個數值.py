def return2num(n=0) :
    x1 = 1
    x2 = 0
    for i in range(1, int(n)+1) :
        x1 *= i
        x2 += i
    return (x1, x2)

x = return2num(input())
print(x[0])
print(x[1])