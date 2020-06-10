class student :
    def __init__(self, name, gender) :
        self.name = name
        self.gender = gender
        self.grades = []

    def avg(self) :
        return sum(self.grades)/len(self.grades)

    def add(self, grade) :
        self.grades.append(grade)

    def fcount(self) :
        f = 0
        for i in self.grades :
            if i < 60 :
                f += 1
        return f

    def show(self) :
        print(self.name)
        print('%.2f' %self.avg())
        print(self.fcount())

s = student(str(input()), str(input()))
s.add(int(input()))
s.add(int(input()))
s.add(int(input()))
s.show()