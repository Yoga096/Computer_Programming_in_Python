class city_and_infect:
    def __init__(self, name, people, infected) :
        self.name = name
        self.people = people
        self.infected = infected

class virus :
    city_list = []
    global_people = 0
    global_infect_num = 0
    global_infect_rate = 0
    
    def __init__(self) :
        #self.city = city
        self.people = 0
        self.total = 1
    
    def add_city(self, city_and_infect):
        self.city_list.append(city_and_infect)
        self.count()

    def infect(self, city, times, spread, separate):
        for i in range(len(self.city_list)) :
            if self.city_list[i].name == city :
                self.people = self.city_list[i].people
                self.total = self.city_list[i].infected
                for j in range(times) :
                    self.total += self.total * (spread - separate)
                if self.total > self.people :
                    self.total = self.people
                self.city_list[i].infected = self.total
                break
        print(city + "'s infected people: %i/%i" %(self.total, self.people))
        self.count()

    def count(self):
        self.global_people = 0
        self.global_infect_num = 0
        self.global_infect_rate = 0
        for i in self.city_list :
            self.global_people += i.people
            self.global_infect_num += i.infected
        self.global_infect_rate = self.global_infect_num / self.global_people 

    def show_detail(self):        
        print("Total: %i" %self.global_people)
        print("current_infected: %i" %self.global_infect_num)        
        print("infected_rate: %.2f" %round(self.global_infect_rate+ 0.0000000001, 2))               
       
        for i in self.city_list :
            print("city name: " + i.name)
            print("people num: %i" %i.people)
            print("current infected: %i" %i.infected)