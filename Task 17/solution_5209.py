import math

with open("Files/5209", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    average = sum(numbers_list) / len(numbers_list)
    total_list = []
    for i in range(len(numbers_list) - 2):
        if numbers_list[i] + numbers_list[i + 1] == int(math.sqrt(numbers_list[i] + numbers_list[i + 1])) ** 2 or\
            numbers_list[i + 1] + numbers_list[i + 2] == int(math.sqrt(numbers_list[i + 1] + numbers_list[i + 2])) ** 2 or\
            numbers_list[i] + numbers_list[i + 2] == int(math.sqrt(numbers_list[i] + numbers_list[i + 2])) ** 2:
            if (numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2]) / 3 > average:
                total_list.append(numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2])
print(len(total_list), max(total_list))
