import time

a = float(input())
x1 = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(a))
x2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a))

print(x1)
print(x2)
