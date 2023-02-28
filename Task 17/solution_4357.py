with open("Files/4357", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    total_list = []
    for number in numbers_list:
        if number % 8 == 7 and (number // 8) % 8 != 2:
            total_list.append(number)
print(len(total_list), max(total_list))
