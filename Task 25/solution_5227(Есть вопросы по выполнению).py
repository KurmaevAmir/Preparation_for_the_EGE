import math

count = 0
k = 1
while count != 5:
    n = 500000000 + k
    intermediate_list = []
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            intermediate_list.append(j)
            if n // j != j:
                intermediate_list.append(n // j)
    if len(intermediate_list) != 3 and len(intermediate_list) > 0:
        print(k, max(intermediate_list))
        count += 1
    k += 1
