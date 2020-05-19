def swap(x) :
    x.reverse()
    return x

list = []
list.append(int(input()))
list.append(int(input()))

for i in swap(list) :
    print(i)

