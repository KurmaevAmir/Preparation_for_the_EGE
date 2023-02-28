with open("Files/4899", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    sum_numbers = []
    for number in numbers_list:
        if number > 0:
            sum_numbers.append(number)
    average = sum(sum_numbers) / len(sum_numbers)
    total_list = []
    for i in range(len(numbers_list) - 1):
        if numbers_list[i] > average or numbers_list[i + 1] > average:
            sum_number1 = sum([int(i) for i in str(abs(numbers_list[i]))])
            sum_number2 = sum([int(i) for i in str(abs(numbers_list[i + 1]))])
            total_list.append(max(sum_number2, sum_number1))
print(len(total_list), max(total_list))
