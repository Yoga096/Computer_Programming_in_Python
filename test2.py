from Q4_class import virus
 
people = eval(input())
city = input()
Coronavirus = virus(people, city)
 
in_str = input()
while in_str != "q":
    t, s1, s2 = [int(i) for i in in_str.split(" ")]
    Coronavirus.infect(times=t, spread=s1, separate=s2)
    in_str = input()
Coronavirus.show_detail()