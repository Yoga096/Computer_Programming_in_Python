score = [[76, 73, 85], [88, 84, 76], [92, 82, 92], [82, 91, 85], [72, 74, 73]]
sum_t = 0
max_avg = 0
for i in range(5) :
    print("student", i+1)
    print(" 1:", score[i][0])
    print(" 2:", score[i][1])
    print(" 3:", score[i][2])
    sum = score[i][0] + score[i][1] + score[i][2]
    print(" sum:", sum)
    avg = sum / 3
    print(" avg: %.2f" % avg)
    sum_t += sum
    if avg >= max_avg :
        max_avg = avg
        max = i + 1

avg_t = sum_t / 15
print("total: ", sum_t, ", avg: %.2f" % avg_t, sep = "")
print("highest avg: student ", max, ": %.2f" % max_avg, sep = "" )