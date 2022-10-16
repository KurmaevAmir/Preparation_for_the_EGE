# import math
#
#
# def check_number(n):
#     if n < 10:
#         if n in [2, 3, 5, 7]:
#             return True
#         return False
#     if n % 2 == 0 or n % 10 == 5:
#         return False
#     for z in range(3, int(math.sqrt(n)) + 1):
#         if n % z == 0:
#             return False
#     return True
#
#
# count = 0
# for i in range(50222022 + 1, 20222022, - 1):
#     sum_numbers_i = sum([int(j) for j in str(i)])
#     if sum_numbers_i % 22 == 0:
#         interior_count = 0
#         for j in range(2, int(math.sqrt(int(math.factorial(sum_numbers_i)))) + 1):
#             if sum_numbers_i % j == 0:
#                 if check_number(j):
#                     interior_count += 1
#                 if sum_numbers_i // j != j and check_number(sum_numbers_i // j):
#                     interior_count += 1
#         if interior_count % 2022 == 0 and interior_count != 0:
#             count += 1
#             print(i, interior_count)
#             if count == 5:
#                 break
import math

primes_list = [2]
for i in range(3, 50222022 + 1, 2):
    if i > 10 and i % 10 == 5:
        continue
    for j in primes_list:
        if j > int(math.sqrt(i) + 1):
            primes_list.append(i)
            break
        if i % j == 0:
            break
    else:
        primes_list.append(i)

count = 0
for i in range(50222022 + 1, 20222022, - 1):
    sum_numbers_i = sum([int(j) for j in str(i)])
    if sum_numbers_i % 22 == 0:
        interior_count = 0

