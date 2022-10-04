import math

stop = 912673 - 2
count = 0
black_list = []
# for i in range(2, int(math.sqrt(stop)) + 1):
#     if i > 10:
#         if i % 2 == 0 or i % 10 == 5:
#             continue
#     for j in black_list:
#         if j > int((math.sqrt(i)) + 1):
#             black_list.append(i)
#             break
#         if i % j == 0:
#             break
#     else:
#         black_list.append(i)
for i in range(2, stop + 1):
    if i > 10:
        if i % 2 == 0 or i % 10 == 5:
            continue
        else:
            cond = True
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    cond = False
                    break
            if cond:
                black_list.append(i)
    elif i < 10 and i in [2, 3, 5, 7]:
        black_list.append(i)

while count != 5:
    intermediate_list = []
    for j in range(2, int(math.sqrt(stop)) + 1):
        if stop % j == 0:
            if j not in black_list:
                intermediate_list.append(j)
            if stop // j != j and (stop // j) not in black_list:
                intermediate_list.append(stop // j)
    if bool(intermediate_list):
        s = sum(intermediate_list)
        if stop % s == 0:
            count += 1
            print(stop, s)
    stop -= 2
