def Matrix_T(MatrixA) :
    for i in range(len(MatrixA[0])) :
        for j in range(len(MatrixA)-1) :
            print(MatrixA[j][i], end = " ")
        print(MatrixA[j+1][i])

m = []
while True :
    x = str(input())
    if x != "q" :
        m.append(x.split())
    else :
        break

Matrix_T(m)