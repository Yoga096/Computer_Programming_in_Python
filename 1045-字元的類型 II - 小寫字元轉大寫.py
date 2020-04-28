x = str(input())
if x.isdigit() == True :
    print(x, "is a number.")
elif x.isupper() == True :
    print(x, "is a capital letter.")
elif x.islower() == True :
    print(x, "is a lowercase letter.")
    print("swap to capital letter " + x.upper() + ".")
else :
    print(x, "is a punctuation.")