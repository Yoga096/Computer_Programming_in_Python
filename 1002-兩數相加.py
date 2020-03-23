# 輸入兩個小數, 印出兩者相加的結果(※輸出小數後兩位)

x1 = float(input())
x2 = float(input())

print ("%.2f" %x1, "+",
       "%.2f" %x2, "=",
       "%.2f" %(x1 + x2))