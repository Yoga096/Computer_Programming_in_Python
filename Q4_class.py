class virus :
    def __init__(self, people, city) :
        self.city = city
        self.people = people
        if people >= 1 :
            self.total = 1
        else :
            self.total = 0
    
    def infect(self, times, spread, separate):
        if (spread >= 0) & (separate >= 0) :
            if times > 0 :
                for i in range(times) :
                    self.total += self.total * (spread - separate)
                if self.total > self.people :
                    self.total = self.people
            print(self.city + "'s infected people: %i/%i" %(self.total, self.people))
    
    def show_detail(self):
        print("city name: " + self.city)
        print("people num: %i" %self.people)
        print("current infected: %i" %self.total)