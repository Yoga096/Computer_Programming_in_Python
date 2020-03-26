# 如果 N 是 7的倍數或者是那個數字裏含有‘7’
# 這個號碼就是 "YES", 反之 "NO"。 

N = str(input())

if int(N) % 7 == 0 :

    print("YES")

elif "7" in N :

    print("YES")

else :

    print("NO")