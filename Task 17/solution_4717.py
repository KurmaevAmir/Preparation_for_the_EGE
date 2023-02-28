with open("Files/4717", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    sum_numbers = 0
    for number in numbers_list:
        if number % 51 == 0:
            sum_numbers += sum([int(i) for i in str(number)])
    total_list = []
    for i in range(len(numbers_list) - 1):
        if numbers_list[i] < sum_numbers or numbers_list[i + 1] < sum_numbers:
            total_list.append(numbers_list[i] + numbers_list[i + 1])
print(len(total_list), max(total_list))
