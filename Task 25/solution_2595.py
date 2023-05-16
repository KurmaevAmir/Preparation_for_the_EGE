import math

total_list = []
for i in range(4099, 26986):
    count = 0
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            count += 1
            if i // j != j:
                count += 1
    if count == 1:
        sum_number = 0
        for j in str(abs(i)):
            sum_number += int(j)
        total_list.append(sum_number)
print(len(total_list), sum(total_list))
