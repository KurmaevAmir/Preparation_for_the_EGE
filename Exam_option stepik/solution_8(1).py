from itertools import product

count = 0
numbers_list = list(product("01234567", repeat=5))
numbers_list = [int("".join([j for j in massive])) for massive in numbers_list if massive[0] != "0"]
for number in numbers_list:
    if str(number).count("6") == 1:
        index = str(number).index("6")
        if index == 0:
            if int(str(number)[1]) % 2 == 0:
                count += 1
        elif index == len(str(number)) - 1:
            if int(str(number)[len(str(number)) - 2]) % 2 == 0:
                count += 1
        else:
            if int(str(number)[index - 1]) % 2 == 0 and int(str(number)[index + 1]) % 2 == 0:
                count += 1
print(count)
