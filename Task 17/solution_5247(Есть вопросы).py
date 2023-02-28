with open("Files/5247", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    sum_numbers = 0
    count = 0
    for number in numbers_list:
        if number % 31 == 0:
            sum_numbers += number
            count += 1
    average = sum_numbers / count
    total_list = []
    for i in range(len(numbers_list) - 2):
        sum_number = numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2]
        remainder_list = []
        while sum_number // 5 > 0:
            remainder_list.append(str(sum_number % 5))
            sum_number //= 5
        remainder_list.append(str(sum_number))
        sum_number = "".join(remainder_list)
        if len(sum_number) % 2 == 0:
            if sum_number[len(sum_number) // 2:] == sum_number[:len(sum_number) // 2]:
                if (numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2]) / 3 > average:
                    total_list.append(numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2])
        else:
            if sum_number[len(sum_number) // 2 + 1:] == sum_number[:len(sum_number) // 2]:
                if (numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2]) / 3 > average:
                    total_list.append(numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2])
print(len(total_list), min(total_list))
