dict = {"P" : "Pikachu", 
        "M" : "Mickey Mouse", 
        "H" : "Hello kitty"}

while True :
    x = str(input())
    if x == "-1" :
        break
    elif x in dict :
        print(dict[x])
    else :
        print(x, "does not exist. Enter a new one:")
        dict[x] = str(input())