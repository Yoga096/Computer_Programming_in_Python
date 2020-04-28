dic = {"1" : "I",
       "7" : "T", 
       "3" : "E", 
       "5" : "S", 
       "4" : "A", 
       "0" : "O"}

ans = ""
for i in str(input()) :
    if i in ["1", "7", "3", "5", "4", "0"] :
        ans += dic[i]
    else :
        ans += i
print(ans)