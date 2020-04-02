h = float(input()) * 0.01
w = float(input())
bmi = w / (h ** 2)
print("%.2f" %bmi)
if bmi < 18.5 :
    print("Underweight")
elif (bmi >= 18.5) & (bmi < 24) :
    print("Normal")
elif (bmi >= 24) & (bmi < 27) :
    print("Overweight")
elif (bmi >= 27) & (bmi < 30) :
    print("Obese Class I")
elif (bmi >= 30) & (bmi < 35) :
    print("Obese Class II")
else :
    print("Obese Class III")