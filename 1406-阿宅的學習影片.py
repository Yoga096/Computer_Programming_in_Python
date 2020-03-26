# 已知，片的重點從影片的第L秒開始，而現在阿宅在影片的第S秒。
# 已知阿宅按一次快轉會快轉5秒，而如果超過了第L秒阿宅就需要倒帶,按倒帶一次會回去前2秒。
# PS:如果現在阿宅在1秒，但是他要按倒帶的話，會不成功,因爲影片沒有負數秒。所以那次的操作不算。
# 請問阿宅需要最少按幾次才能到達第L秒呢？

rush = 5
back = 2
LS = input().split()
L = int(LS[0])
S = int(LS[1])
gap = L - S
x = 0

while True :
    
    if gap > 0 :

        x += 1
        gap -= 5
       
    elif gap < 0 :

        x += 1
        gap += 2
        
    else :
        break

print(x)

