import pandas as pd

s = pd.read_csv("./" + str(input()))
s["avg"] = (s["exam01"] + s["exam02"] + s["exam03"] + s["exam04"]) * 0.7/4 + (s["homework"]*0.3/0.4)
s[(s.avg < 60 ) & (s.homework == 40)]["avg"].apply(lambda x : 60.0)

for i in range(len(s)) :
    print(s["student number"][i], "%.2f" %s["avg"][i])