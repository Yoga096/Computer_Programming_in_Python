x = int(input())
if x >= 90 :
    g = "4.3"
    a = "A+"
elif x >= 85 :
    g = "4.0"
    a = "A"
elif x >= 80 :
    g = "3.7"
    a = "A-"
elif x >= 77 :
    g = "3.3"
    a = "B+"
elif x >= 73 :
    g = "3.0"
    a = "B"
elif x >= 70 :
    g = "2.7"
    a = "B-"
elif x >= 67 :
    g = "2.3"
    a = "C+"
elif x >= 63 :
    g = "2.0"
    a = "C"
elif x >= 60 :
    g = "1.7"
    a = "C-"
else :
    g = "0"
    a = "F"

print(g)
print(a)