m = int(input())
slen = int(input())
s = []
for i in range(slen) :
    s0 = []
    for x in str(input()).split(",") :
        s0.append(int(x))
    s.append(s0)

for i in range(m) :
    line = ""
    for j in range(m) :
        if [i+1, j+1] in s :
            line += "0 "
        else :
            line += "- "
    print(line)

print(s)
while True :
    x = str(input())
    if x == "q" :
        break
    
    else :
        if slen > 1 :
            for i in range(slen-1) :
                s[i][0] = s[i+1][0]
                s[i][1] = s[i+1][1]
        
        if x == "right" :    
            s[-1][1] += 1
        
        elif x == "left" :
            s[-1][1] -= 1
        
        elif x == "up" :
            s[-1][0] -= 1
                
        elif x == "down" :
            s[-1][0] += 1
       
        print(s)

for i in range(m) :
    line = ""
    for j in range(m) :
        if [i+1, j+1] in s :
            line += "0 "
        else :
            line += "- "
    print(line)
