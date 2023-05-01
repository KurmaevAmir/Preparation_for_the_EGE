with open("Files/17.txt", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    max_number = -float('inf')
    total_list = []
    for number in numbers_list:
        if len(str(number)) == 2:
            max_number = max(max_number, number)
    for i in range(len(numbers_list) - 1):
        if len(str(numbers_list[i])) == 2 and len(str(numbers_list[i + 1])) != 2 and \
                (numbers_list[i] + numbers_list[i + 1]) % max_number == 0:
            total_list.append(numbers_list[i] + numbers_list[i + 1])
        elif len(str(numbers_list[i])) != 2 and len(str(numbers_list[i + 1])) == 2 and \
                (numbers_list[i] + numbers_list[i + 1]) % max_number == 0:
            total_list.append(numbers_list[i] + numbers_list[i + 1])
print(len(total_list), max(total_list))
