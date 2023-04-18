massive = [0] * 101
massive[3] = 1
total_list = []
for i in range(4, 101):
    if i - 3 >= 3:
        a = massive[i - 3]
        if i % 3 == 0 and i // 3 >= 3:
            a += massive[i // 3]
        if i % 2 == 0 and a != 0:
            total_list.append(i)
        massive[i] = a
print(len(total_list))
