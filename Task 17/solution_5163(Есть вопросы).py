with open("Files/5163", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    max_number = -float('inf')
    for number in numbers_list:
        if number % 51:
            max_number = max(max_number, number)
    total_list = []
    for i in range(len(numbers_list) - 1):
        if numbers_list[i] == 51 * int(str(numbers_list[i])[-1]) and numbers_list[i + 1] != 51 * int(str(numbers_list[i + 1])[-1]):
            if sum([int(j) for j in str(numbers_list[i])]) + sum([int(j) for j in str(numbers_list[i + 1])]) < max_number:
                total_list.append(numbers_list[i] + numbers_list[i + 1])
        elif numbers_list[i] != 51 * int(str(numbers_list[i])[-1]) and numbers_list[i + 1] == 51 * int(str(numbers_list[i + 1])[-1]):
            if sum([int(j) for j in str(numbers_list[i])]) + sum([int(j) for j in str(numbers_list[i + 1])]) < max_number:
                total_list.append(numbers_list[i] + numbers_list[i + 1])
print(len(total_list), max(total_list))
