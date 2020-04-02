x = str(input())
if x in ["1", "2"] :
    
    y = int(input())
    if (y >= 0) & (y <= 100) :
        
        if (x == "1") & (y >= 60) :
            print("pass")
        elif (x == "2") & (y >= 70) :
            print("pass")
        else :  
            print("fail")
   
    else :
        print("score error")
else :
    print("roll error")
