import math

stop = 299999999


def check_number(n):
    for j in str(n)[:-1]:
        if int(j) % 2 == 0:
            return False
    else:
        return True


count = 0
while count != 5:
    intermediate_list = []
    for j in range(3, int(math.sqrt(stop)) + 1, 2):
        if check_number(j):
            if stop % j == 0:
                intermediate_list.append(j)
                if stop // j != j and check_number(stop // j):
                    intermediate_list.append(stop // j)
    if len(intermediate_list) >= 5:
        print(intermediate_list[-4], len(intermediate_list))
        count += 1
    stop -= 2
