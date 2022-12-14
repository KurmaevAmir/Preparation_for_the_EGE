#Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [180131; 180179],
# числа, имеющие ровно 6 различных делителей.
# В ответе для каждого найденного числа запишите два его наибольших делителя в порядке возрастания.
import math

for i in range(180131, 180180):
    count = 1
    l = []
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            count += 1
            l.append(j)
            if i // j != j:
                count += 1
                l.append(i // j)
        if count > 5:
            break
    if count == 5:
        l.append(i)
        l.sort()
        print(l[-2], l[-1])
