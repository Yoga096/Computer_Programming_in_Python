from Q5_class import virus, city_and_infect
 
Coronavirus = virus()
#print("input type")
in_str = input()
while in_str != "q":
    if in_str == "i":
        city = input()
        t, s1, s2 = [int(i) for i in input().split(" ")]
        Coronavirus.infect(city=city, times=t, spread=s1, separate=s2)
    if in_str == "a":
        name = input()
        people = eval(input())
        infected = eval(input())
        Coronavirus.add_city(city_and_infect(name=name, people=people, infected=infected))
    #print("input type")
    in_str = input()
Coronavirus.show_detail()