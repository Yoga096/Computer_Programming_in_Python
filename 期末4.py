class virus :
    def __init__(self, city, people) :
        self.city = city
        self.people = people
        self.total = 1
    
    def infect(self, times, spread, separate):
        for i in range(times) :
            self.total += self.total * (spread - separate)
        print("Taiwan's infected people: %i/23000000" % self.total)
    
    def show_detail(self):
        print("city name: " + self.city)
        print("people num: %i" %self.people)
        print("current infected: %i" %self.total)

a = virus("Taiwan", 23000000)
a.infect(3, 3, 1)
a.show_detail()