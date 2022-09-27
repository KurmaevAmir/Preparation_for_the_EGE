import math

start = 550000
count = 0
while count != 5:
    intermediate_list = []
    for i in range(2, int(math.sqrt(start)) + 1):
        if start % i == 0:
            intermediate_list.append(i)
            if start // i != i:
                intermediate_list.append(start // i)
    if len(intermediate_list) == 0:
        start += 1
        continue
    else:
        f = sum(intermediate_list) // len(intermediate_list)
    if f % 31 == 13:
        count += 1
        print(start, f)
    start += 1
