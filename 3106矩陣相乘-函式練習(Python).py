def x_in() :
    x = []
    for i in range(3) :
        x.append([])
        for j in str(input()).split(" ") :
            if j.isdigit() :
                x[i].append(int(j))
    return x

def matrixMultiPly(a, b) :
    xx = []
    for i in range(3) :
        xx.append([])
        for j in range(3) :
            xxx = 0
            for k in range(3) :
                xxx += a[i][k] * b[k][j]
            xx[i].append(xxx)
    return xx

a = x_in()
b = x_in()
c = matrixMultiPly(a, b)
for i in c :
    print(i)