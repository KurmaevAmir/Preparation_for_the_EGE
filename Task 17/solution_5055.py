with open("Files/5055", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    min_number = float("inf")
    for number in numbers_list:
        if number % 17 == 0:
            min_number = min(min_number, number)
    total_list = []
    for i in range(len(numbers_list) - 1):
        if numbers_list[i] % min_number == 0 or numbers_list[i + 1] % min_number == 0:
            total_list.append(numbers_list[i] + numbers_list[i + 1])
print(len(total_list), max(total_list))
