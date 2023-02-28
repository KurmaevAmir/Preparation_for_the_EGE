with open("Files/5189", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    min_number = float('inf')
    for number in numbers_list:
        if number % 321 == 0:
            min_number = min(min_number, number)
    total_list = []
    for i in range(len(numbers_list) - 1):
        if len(hex(numbers_list[i])[2:]) % 2 != 0 and len(hex(numbers_list[i + 1])[2:]) % 2 != 0 and numbers_list[i] + numbers_list[i + 1] > min_number:
            total_list.append(numbers_list[i] + numbers_list[i + 1])
    print(len(total_list), min(total_list))
