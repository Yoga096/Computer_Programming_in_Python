def open_file(x, f1) :
    f0 = open("../app/" + x, mode = 'r').read().split(" ")
    for i in f0 :
        if i.isdigit() :
            f1.append(int(i)) 
    return f1

f = []
for i in range(2) :
    f = open_file(str(input()), f)

for i in sorted(f) :
    print(i, end = " ")