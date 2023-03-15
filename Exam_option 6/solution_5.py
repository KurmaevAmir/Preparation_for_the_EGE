for i in range(10000, 100000):
    i_str = str(i)
    sum_i = int(i_str[0]) + int(i_str[2]) + int(i_str[4])
    sum_i2 = int(i_str[1]) + int(i_str[3])
    if sum_i > sum_i2:
        number = str(sum_i2) + str(sum_i)
    else:
        number = str(sum_i) + str(sum_i2)
    if number == '723':
        print(i)
        break
