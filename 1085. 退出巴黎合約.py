class Data:
    Animal_list = []
    type = len(Animal_list)
    def __init__(self, name, number):
        self.name = name
        self.number = number
        if number >= 1000 :
            self.endanger = "No"
        else :
            self.endanger = "Yes"

    def Animal() :
        return []

    def add(x) :
        Animal_list.append(x)
        print("Add. Animal: " + x.name + ".", "Number: " + str(x.number), "Endanger species: " + x.endanger, sep = "\n")
    def update(x) :
        for i in range(len(Animal_list)) :
            if Animal_list[i].name == x.name :
                Animal_list[i] = x
        print("Update. Animal: " + x.name + ".", "Number: " + str(x.number), "Endanger species: " + x.endanger, sep = "\n")
    
    def display() :
        Endanger_a = []
        for i in Animal_list :
            if i.endanger == 'Yes' :
                Endanger_a.append(i)
        print("There are", len(Endanger_a), "animals who are endanger species")
        for i in Endanger_a :
            print("Animal:", i.name + ".")
            print("Number:", i.number)

Animal_list = Data.Animal()
while True :
    x0 = str(input())
    if x0[0] == "a" :
        Data(x0[2:], int(input())).add()
    elif x0[0] == "u" :
        Data(x0[2:], int(input())).update()        
    elif x0 == "d" :
        Data.display()
    else :
        print("That are the endanger animal list we have now. Bye bye.")
        break

