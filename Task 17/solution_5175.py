with open("Files/5175", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    max_number = -float('inf')
    for number in numbers_list:
        if number % 401 == 0:
            max_number = max(max_number, number)
    total_list = []
    for i in range(len(numbers_list) - 2):
        if numbers_list[i] % (sum([int(j) for j in str(numbers_list[i + 1])]) + sum([int(j) for j in str(numbers_list[i + 2])])) == 0 or\
                numbers_list[i + 1] % (sum([int(j) for j in str(numbers_list[i])]) + sum([int(j) for j in str(numbers_list[i + 2])])) == 0 or\
                numbers_list[i + 2] % (sum([int(j) for j in str(numbers_list[i])]) + sum([int(j) for j in str(numbers_list[i + 1])])) == 0:
            if numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2] > max_number:
                total_list.append(numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2])
print(len(total_list), min(total_list))
