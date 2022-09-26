import math

total_count = 0
for i in range(4986, 32599 + 1):
    count = 0
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            count += 1
            if i // j != j:
                count += 1
        if count > 2:
            break
    if count == 2:
        total_count += i
print(total_count)
