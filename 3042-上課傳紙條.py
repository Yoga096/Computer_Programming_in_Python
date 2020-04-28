abc = {"a" : "x",
       "b" : "y",
       "c" : "z",
       "d" : "a",
       "e" : "b",
       "f" : "c",
       "g" : "d",
       "h" : "e",
       "i" : "f",
       "j" : "g",
       "k" : "h",
       "l" : "i",
       "m" : "j",
       "n" : "k",
       "o" : "l",
       "p" : "m",
       "q" : "n",
       "r" : "o",
       "s" : "p",
       "t" : "q",
       "u" : "r",
       "v" : "s",
       "w" : "t",
       "x" : "u",
       "y" : "v",
       "z" : "w"}

ans = ""
while True :
    x = str(input())
    if x == "-1" :
        break       
    else :
        for i in x :
            if i.isalpha() :
                i = i.lower()
                ans += abc[i]
            else :
                ans += i
    ans += " "

print(ans.rstrip())