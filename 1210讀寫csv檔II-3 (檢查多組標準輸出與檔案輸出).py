import csv

n = str(input())
s = open("./stores_old" + n + ".csv", encoding = 'big5').readlines()
with open('stores_new' + n + '.csv', 'w', newline='', encoding = 'utf8') as f :
    s1 = csv.writer(f)
    for i in s :
        x = i.split(",")
        x1 = [x[0], x[3], x[5], x[6], ""]
        s1.writerow(x1)

f.close()

ss = open("./stores_new" + n + ".csv", "r", encoding = 'utf8').readlines()
for i in ss :
    print(i, end = "")