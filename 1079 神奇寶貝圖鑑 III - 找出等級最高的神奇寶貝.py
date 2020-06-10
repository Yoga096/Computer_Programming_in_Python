max_lv = 0
for i in range(3) :
    name = str(input())
    lv = int(input())
    hp = int(input())
    if lv > max_lv :
        max_name = name
        max_lv = lv
        max_hp = hp
        
print("Name: " + max_name, "Lv: " + str(max_lv), "HP: " + str(max_hp), sep= "\n")