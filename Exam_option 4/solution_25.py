import math

global_count = 0
for i in range(489421, 489441):
    count = 0
    divisors_list = []
    cond = True
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            count += 1
            divisors_list.append(j)
            if i // j != j:
                count += 1
                divisors_list.append(i // j)
        if count > 4:
            cond = False
            break
    if cond and count == 4:
        print(" ".join([str(k) for k in divisors_list]))
        global_count += 1
        if global_count == 5:
            break
