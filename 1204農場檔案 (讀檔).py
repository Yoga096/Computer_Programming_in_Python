s = open(str(input())).readlines()
for i in range(1, len(s),2) :
    if int(s[i].split()[0]) >= 50 :
        print(s[i-1].split()[0], s[i].split()[0])