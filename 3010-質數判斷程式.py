n = int(input())
if n == 1 :
    y = "is not prime"
elif n == 2 :
    y = "is prime"
else :
    for i in range(2, n) :
        if n % i == 0 :
            y = "is not prime"
            break
        else :
            y = "is prime"

print(n, y)