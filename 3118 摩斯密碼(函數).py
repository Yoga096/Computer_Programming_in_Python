dict = {'-----' : '0', '.----' : '1', '..---' : '2', '...--' : '3', '....-' : '4', '.....' : '5', '-....' : '6', '--...' : '7', '---..' : '8', '----.' : '9'}

def transform(lst, a = "") :
    for i in lst :  
        while " " in i :
            i = i[1:]
        if i in dict :
            a += dict[i]
        else :
            a = "error"
            break
    return(a)      

xl = []
while True :
    x = str(input())
    if x != "-1" : 
        xl.append(x.split())

    else :
        break

for i in xl :
    print(transform(i))   
