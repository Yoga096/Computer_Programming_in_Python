abc = "abcdefghijklmnopqrstuvwxyz"

for i in str(input()).split("-") :
    print(abc[(int(i) % 26)-1] * ((int(i)+25) // 26), end="")     