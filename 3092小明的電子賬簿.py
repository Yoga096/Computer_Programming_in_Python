s = open("../app/" + str(input())).readlines()
t = 0
for i in range(1, len(s), 2) :
    print("chef", s[i-1][:-1], end = " ")
    if "\n" in s[i] :    
        print(s[i][:-1])
        t += int(s[i][:-1])
    else :
        print(s[i])
        t += int(s[i])
print("Total:", t)
print("Avg:", "%.2f" %(t * 2/len(s)))