def is_int(i):
    try:
        int(i)
        return True
    except ValueError:
        pass

def is_float(i):
    try:
        float(i)
        return True
    except ValueError:
        pass


list1 = []
while True :
    x = str(input())
    if x == "q" :
        break    
    else :
        if is_int(x) == True :
            list1.append(int(x))
        elif is_float(x) == True :
            list1.append(float(x))
        else :
            print("Please Enter Numbers Only")

print(list1)

list2 = sorted(list1)
print(list2)

list2.reverse()
print(list2)

print(list1)