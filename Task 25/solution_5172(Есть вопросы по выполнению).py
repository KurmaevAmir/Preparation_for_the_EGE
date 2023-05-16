from solution_5227 import function

print(function(50027512))

count = 0
a = 0
for j in range(2, 50222022 + 1):
    a += len(function(j))
print(a)
for i in range(50222022, 20222022 - 1, - 1):
    sum_number = sum([int(j) for j in str(i)])
    if sum_number % 22 == 0:
        print(i)
        a = 0
        for j in range(2, i + 1):
            a += len(function(j))
        print(a)
        if a % 2022 == 0:
            print(i, a)
            count += 1
    if count == 5:
        break
