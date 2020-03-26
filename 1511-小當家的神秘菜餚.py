# 加熱一分鐘可以使菜餚的溫度提高 X 攝氏度，
# 而冷卻一分鐘會使菜餚溫度下降 Y 攝氏度。
# 加熱一分鐘后必須冷卻一分鐘，所以不能連續加熱。
# 小當家最多衹有 N 分鐘可以準備他的菜餚。
# 這道菜餚要越熱越好，所以請問在規定的時間N 内小當家最多可以把菜餚加熱到多少攝氏度呢？

NXY = str(input()).split()
N = int(NXY[0])
X = int(NXY[1])
Y = int(NXY[2])
ans = 20

if N % 2 == 0 :

    ans += X * (N // 2)
    ans -= Y * ((N // 2) - 1)

else :

    ans += X * ((N // 2) + 1)
    ans -= Y * (N // 2)

print(ans)