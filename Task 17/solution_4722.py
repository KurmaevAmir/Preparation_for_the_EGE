with open("Files/4722", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    sum_numbers = 0
    for number in numbers_list:
        if number % 35 == 0:
            sum_numbers += sum([int(i) for i in str(number)])
    total_list = []
    for i in range(len(numbers_list) - 1):
        if numbers_list[i] > sum_numbers and numbers_list[i + 1] <= sum_numbers:
            if hex(numbers_list[i + 1])[-2:] == "ef":
                total_list.append(numbers_list[i] + numbers_list[i + 1])
        elif numbers_list[i] <= sum_numbers and numbers_list[i + 1] > sum_numbers:
            if hex(numbers_list[i])[-2:] == "ef":
                total_list.append(numbers_list[i] + numbers_list[i + 1])
print(len(total_list), min(total_list))
