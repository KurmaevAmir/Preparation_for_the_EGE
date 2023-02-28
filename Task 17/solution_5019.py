with open("Files/5019", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    sum_numbers = 0
    for number in numbers_list:
        sum_numbers += oct(number).count("7") * 7
    total_list = []
    for i in range(len(numbers_list) - 1):
        if numbers_list[i] > sum_numbers and numbers_list[i + 1] > sum_numbers:
            total_list.append(numbers_list[i] + numbers_list[i +1])
print(len(total_list), min(total_list))
