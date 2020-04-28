x = str(input()).upper()
all = []
while True :
    i = str(input()).upper()
    if i == "Q" :
        break
    else :
        all.append(i)

if x in all :
    print("Yes", all.index(x) + 1)
else : 
    print("No", len(all))