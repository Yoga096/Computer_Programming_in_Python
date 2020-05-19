s = open("./" + str(input())).readlines()
r, e = 0, 0
for i in s[1:] :
    i = i.split(",")
    if i[-1][0] != "F" :
        if i[1] == "R" :
            r += int(i[2])
        else :
            e += int(i[2])

print("Required:", r)
print("Elective:", e)

if (r >= 72) & (e >= 28) :
    print("Y")
else :
    print("N")
    print("Student still needs to complete ", end = "")
    if (r < 72) & (e < 28) :
        print(72 - r, "required credits &", 28 - e, "elective credits for graduation.")
    elif  r >= 72 :
        print(28 - e, "elective credits for graduation.")
    else :
        print(72 - r, "required credits for graduation.")