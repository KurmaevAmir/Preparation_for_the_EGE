import math

count = 0
for i in range(800001, 900000):
    definitive_list = []
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            definitive_list.append(j)
            if i // j != j:
                definitive_list.append(i // j)
    if len(definitive_list) > 10 and sum(definitive_list) % 2 != 0:
        product = 1
        for j in range(len(definitive_list)):
            product *= definitive_list[j]
        if product % 2 != 0:
            print(i, len(definitive_list))
            count += 1
            if count == 6:
                break
