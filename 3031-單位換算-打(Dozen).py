# 今天令使用者輸入一個整數(int)，我們將數字轉換成打(Dozen)。
# 例如：25 = 2 dozen and 1

n = int(input())
a = ""
d = str(n // 12)
da = n % 12

if da != 0 :
    a = str(" and " + str(da))

print(d, "dozen" + a) 

