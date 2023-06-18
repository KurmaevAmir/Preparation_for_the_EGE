import math

count = 0
for i in range(452022, 10 ** 8):
    m = 0
    divisors_list = []
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            divisors_list.append(j)
            if i // j != j:
                divisors_list.append(i // j)
    if len(divisors_list) > 1:
        m = max(divisors_list) + min(divisors_list)
        if m % 7 == 3:
            print(i, m)
            count += 1
            if count == 5:
                break
