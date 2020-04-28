n = int(input())
all = []
score = {}
ans = ""
score_max = 0

dict = {"A" : 1,
        "B" : 2,
        "C" : 3,
        "D" : 4,
        "E" : 5,
        "F" : 6,
        "G" : 7,
        "H" : 8,
        "I" : 9,
        "J" : 10,
        "K" : 11,
        "L" : 12,
        "M" : 13,
        "N" : 14,
        "O" : 15,
        "P" : 16,
        "Q" : 17,
        "R" : 18,
        "S" : 19,
        "T" : 20,
        "U" : 21,
        "V" : 22,
        "W" : 23,
        "X" : 24,
        "Y" : 25,
        "Z" : 26} 

for i in range(n) :
    x = str(input()).upper()
    all.append(x)

for i in all :
    score_now = 0
    for j in i :
        score_now += dict[j]
    score[i] = score_now
    if score_now > score_max :
        ans = i
        score_max = score_now

for i in all :
    print(i, "=", score[i])
print(ans, "is the key.")