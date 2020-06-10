class student :
    def __init__(self, name, gender) :
        self.name = name
        self.gender = gender
        self.grades = []
        self.a = 0

    def avg(self) :
        self.a = (sum(self.grades)/len(self.grades))
        return self.a

    def add(self, grade) :
        self.grades.append(grade)

    def fcount(self) :
        f = 0
        for i in self.grades :
            if i < 60 :
                f += 1
        return f
    
    def show(self) :
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Grades:", self.grades)
        print("Avg: %.1f" % self.avg())
        print("Fail Number:", self.fcount())
        print()

def top(*s) :
    max = 0
    for i in s :
        if i.a > max :
            stop = i
            max = i.a
    return stop

s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)

s1.show()
s2.show()
s3.show()
s4.show()
s5.show()
top_student = top(s1,s2,s3,s4,s5)
print("Top Student:")
top_student.show()  
