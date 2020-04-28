dict = {"T" : "Top",
        "H" : "Hoodie",
        "B" : "Backpack"}

while True :
    x = str(input())
    if x == "-1" :
        break
    elif x == "-2" :
        k = sorted(list(dict.keys()))
        v = []
        for i in k :
            v.append(dict[i])
        print("keys:", k)
        print("values:", v)
    elif x == "-3" :
        y = str(input())
        if y in dict :
            del dict[y]
        else :
            print("key", y, "does not exist, cannot delete.")
    elif x in dict :
        print(dict[x])
    else :
        print(x, "does not exist. Enter a new product category:")
        dict[x] = str(input())
