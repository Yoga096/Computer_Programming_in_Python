# 原始分數開根號乘以10

import math

O = float(input())
A = "%.3f" %(math.sqrt(O) * 10)


if A[-1] in ["5", "6", "7", "8", "9"] :
    Ad = float(A[:-1]) + 0.01
else :
    Ad = float(A[:-1])


if A[-3] in ["5", "6", "7", "8", "9"] :
    A1 = math.ceil(float(A))
else :
    A1 = math.floor(float(A))


print("Original:", "%.2f" %O)
print("Adjusted:", "%.2f" %Ad + "(+" + str(int(A1 - O)) + ")")