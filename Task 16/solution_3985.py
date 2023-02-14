funtion_list = [0] * 1001
funtion_list[0] = 0
for i in range(1, 1001):
    if i % 2 == 0:
        funtion_list[i] = funtion_list[i // 2]
    else:
        funtion_list[i] = funtion_list[i - 1] + 3
print(funtion_list.count(18))
