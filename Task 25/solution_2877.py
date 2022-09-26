numbers_list = []
for i in range(57888, 74556):
    if int(str(i)[0]) % 2 != 0 and int(str(i)[1]) % 2 != 0 and \
            int(str(i)[2]) % 2 == 0 and int(str(i)[3]) % 2 == 0 and i % 2 == 0:
        if i % 7 != 0 and i % 9 != 0 and i % 13 != 0:
            numbers_list.append(i)
print(len(numbers_list), (max(numbers_list) - min(numbers_list)))
