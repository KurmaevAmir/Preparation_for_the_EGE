with open("Files/4419", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    total_list = []
    for i in range(1, len(numbers_list) - 1):
        if len(str(numbers_list[i])) == 2 and numbers_list[i] > 0 and numbers_list[i] % 2 != 0:
            total_list.append(numbers_list[i - 1] + numbers_list[i] + numbers_list[i + 1])
print(len(total_list), max(total_list))
