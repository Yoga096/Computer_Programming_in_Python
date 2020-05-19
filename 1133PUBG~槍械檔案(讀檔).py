def open_file(x, a1 = 0, a2 = 0, a3 = 0, a4 = 0, a5 = 0) :
    f0 = open(x, mode = 'r').readlines()
    for i in f0 :
        if "PISTOL" in i :
            a1 += 1
        elif "SMG" in i :
            a2 += 1
        elif "SHOTGUN" in i :
            a3 += 1
        elif "AR" in i :
            a4 += 1
        elif "SNIPER" in i :
            a5 += 1  
        elif "EOF" == i :
            break
    print(a1, a2, a3, a4, a5)

open_file(str(input()))