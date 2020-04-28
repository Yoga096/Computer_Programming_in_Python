x = []
for i in range(5) :
    x.append(int(input()))

for i in x :
    print(i, str("*" * i), sep = "\t")