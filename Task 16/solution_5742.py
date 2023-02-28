from math import sqrt

number = 107864
count = 0
for i in range(3, int(sqrt(number)) + 1):
    if number % i == 0:
        count += 1
        if number // i != i:
            count += 1
print(count + 2)
