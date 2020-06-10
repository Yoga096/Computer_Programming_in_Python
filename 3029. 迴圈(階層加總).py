while True :
    try :
        x = int(input())
        if x > 0 :
            a = 0
            a0 = 1
            for i in range(1, x+1) :
                a0 *= i
                a += a0
            print(a) 
            break
        else :
            pass
    except :
        pass