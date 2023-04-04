def change_base(n):
    remainder_list = []
    while n // 5 > 0:
        remainder_list.append(str(n % 5))
        n //= 5
    remainder_list.append(str(n))
    return "".join(remainder_list)


total_list = []
with open("Files/17", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    sum_numbers = 0
    count = 0
    for i in range(len(numbers_list)):
        if numbers_list[i] % 17 != 0:
            sum_numbers += numbers_list[i]
            count += 1
    average_number = sum_numbers / count
    for i in range(len(numbers_list) - 2):
        numbers_sum = numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2]
        numbers_sum = change_base(numbers_sum)
        if len(numbers_sum) % 2 == 0:
            if numbers_sum[:len(numbers_sum) // 2] != numbers_sum[len(numbers_sum) // 2:][::-1]:
                continue
        else:
            if numbers_sum[:len(numbers_sum) // 2] != numbers_sum[len(numbers_sum) // 2 + 1:][::-1]:
                continue
        max_number = max(numbers_list[i], numbers_list[i + 1], numbers_list[i + 2])
        if max_number < average_number:
            total_list.append(numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2])
print(len(total_list), max(total_list))
