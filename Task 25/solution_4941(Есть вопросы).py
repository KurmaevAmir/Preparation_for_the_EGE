import math

stop = 100000000 - 2
count = 0
while count != 5:
    intermediate_list = []
    for j in range(2, int(math.sqrt(stop)) + 1):
        if stop % j == 0:
            if j % 2 == 0:
                intermediate_list.append(j)
            if stop // j != j:
                if stop // j % 2 == 0:
                    intermediate_list.append(stop // j)
    if len(intermediate_list) >= 5:
        intermediate_list.sort()
        print(intermediate_list[-5], len(intermediate_list))
        count += 1
    stop -= 2
