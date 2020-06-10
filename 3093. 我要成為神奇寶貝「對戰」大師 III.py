class Pokemon :
    def __init__(self, name, lv, hpc) :
        self.Name = name
        self.Lv = lv
        self.MaxHp = hpc
        self.HpCurrent = hpc

    def Pokemon(self, name, lv, hpc) :
        self.Name = name
        self.Lv = lv
        self.HpCurrent = hpc

    def Attack(self, p2) :
        if (self.HpCurrent > 0) & (p2.HpCurrent > 0) :
            p2.HpCurrent -= self.Lv
            print(self.Name, "Attack", p2.Name ,str(self.Lv), "Points.")
            p2.Defence(self)       

    def Defence(self, p2) :
        if self.HpCurrent <= 0 :
            self.HpCurrent = 0
            print(self.Name, "Seriously Injured.")
            print(p2.Name, "Win,", self.Name, "Lose.")
            print(self.Name, "is unable to attack.")

    def Cure(self) :
        pass

    def setData(self, name, lv, hp) :
        pass

    def ShowInfo(self) :
        print("Name:", self.Name)    
        print("Lv:", self.Lv)    
        print("HP: %i/%i" %(self.HpCurrent, self.MaxHp))        


boss = Pokemon("Mewtwo", 30, 300)
n = int(input())

for i in range(n) :
    x = Pokemon(str(input()), int(input()), int(input()))
    boss.Pokemon("Mewtwo", 30, 300)
    print("#%i" %(i+1))
    while (x.HpCurrent > 0) & (boss.HpCurrent > 0) :
        x.Attack(boss)
        #boss.Defence(x)
        boss.Attack(x)
        #x.Defence(boss)
    boss.ShowInfo()
    x.ShowInfo()
    print()
    
