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
    
    def __init__(self, people, city) :
        self.city = city
        self.people = people
        self.total = 1
    
    def add_city(self, city_and_infect):
        self.city_list.append(city_and_infect)
        self.count()

    def infect(self, times, spread, separate):
        if (spread >= 0) & (separate >= 0) :
            if times > 0 :
                for i in range(times) :
                    self.total += self.total * (spread - separate)
                if self.total > self.people :
                    self.total = self.people
            print(self.city + "'s infected people: %i/%i" %(self.total, self.people))
            self.count()

    def count(self):
        self.global_people = 0
        self.global_infect_num = 0
        self.global_infect_rate = 0
        for i in self.city_list :
            self.global_people += i.people
            self.global_infect_num += i.infected
        self.global_infect_rate = self.global_infect_num / self.global_infect_num 

    def show_detail(self):
        
        print("Total: %i" %self.global_people)
        print("current_infected: %i" %self.global_infect_num)        
        print("infected_rate: %.2f" %round(self.global_infect_rate+ 0.0000000001, 2))               
       
        for i in self.city_list :
            print("city name: " + i.city)
            print("people num: %i" %i.people)
            print("current infected: %i" %i.total)