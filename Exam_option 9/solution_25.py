import math

total_list = []
for i in range(120115, 120200 + 1):
    count = 0
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            count += 1
            if i // j != j:
                count += 1
    total_list.append((count, i))
total_list.sort()
print(*total_list[-1])
