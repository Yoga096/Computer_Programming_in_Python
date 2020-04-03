n = int(input())
m = int(input())
for i in range(1, n + 1) :
    x = ""
    for j in range(1, m + 1) :
        x += (str(i) + "*" + str(j) + "=" + "%2i " %(i*j))
    print(x)