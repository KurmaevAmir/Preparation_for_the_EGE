with open("Files/4423", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    total_list = []
    for i in range(1, len(numbers_list) - 1):
        if (numbers_list[i] > 0 and str(numbers_list[i])[-1] == "9") and \
            not(numbers_list[i - 1] > 0 and str(numbers_list[i - 1])[-1] == "9") and \
                not(numbers_list[i + 1] > 0 and str(numbers_list[i + 1])[-1] == "9"):
            total_list.append(numbers_list[i - 1] + numbers_list[i] + numbers_list[i + 1])
print(len(total_list), max(total_list))
