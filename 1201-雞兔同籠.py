# 舉例：
# 現在王老先生看到5個頭，14只脚，
# 所以雞就有3只，兔子有2只。
# 如果王老先生看到的數量無解，就輸出 "NO"

nm = input().split()
n = int(nm[0])
m = int(nm[1])

if (m % 2 == 0) & (n * 2 <= m) & (n * 4 >= m) :
    
    print("YES")

    r = int((m - (n * 2)) / 2)
    c = n - r
    print(c, r)
    
else :
    print("NO")