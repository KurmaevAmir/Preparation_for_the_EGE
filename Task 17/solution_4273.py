pos_last_local_max = 0
local_max_list = []
with open('Files/4273', "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    for i in range(1, len(numbers_list) - 1):
        if numbers_list[i] > numbers_list[i - 1] and numbers_list[i] > numbers_list[i + 1]:
            local_max_list.append((numbers_list[i], i - pos_last_local_max))
            pos_last_local_max = i
local_max_list.sort(key=lambda x: x[1])
print(len(local_max_list), local_max_list[0][1])
