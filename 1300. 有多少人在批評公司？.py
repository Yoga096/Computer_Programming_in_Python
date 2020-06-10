class worker :
    def __init__(self, n, ai, bi, ci) :
        self.n = n
        self.ai = ai
        self.bi = bi
        self.ci = ci

    def attack(self, co) :
        if (self.ai > co.ai) & (self.bi > co.ci) :
            w.remove(co)
            a.append(co)

w = []
number = int(input())
for i in range(number) :
    x = str(input()).split()
    w.append(worker(i+1, int(x[0]), int(x[1]), int(x[2])))
s = int(input())
a = [w[s-1]]
w.remove(w[s-1])

a0 = 0
while a0 != len(a) :
    a0 = len(a)
    for i in a :
        for j in w :
            i.attack(j)
print(a0)