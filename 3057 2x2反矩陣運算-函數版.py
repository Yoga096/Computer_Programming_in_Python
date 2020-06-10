def Matrix_Inverse(MatrixA) :
    a, b, c, d = float(m[0][0]), float(m[0][1]), float(m[1][0]), float(m[1][1])
    dif = 10**-13
    det = a*d - b*c
    if det != 0 :
        print("%.1f" %round((d / det) + dif, 1), "%.1f" %round((-b / det) + dif, 1))
        print("%.1f" %round((-c / det) + dif, 1), "%.1f" %round((a / det) + dif, 1))
        
    else : 
        print("none")       

m = [str(input()).split()]
m.append(str(input()).split())
Matrix_Inverse(m)