with open("Files/4537", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    total_list = []
    for i in range(len(numbers_list) - 1):
        if numbers_list[i] % 7 == 0 or numbers_list[i + 1] % 7 == 0:
            if (numbers_list[i] + numbers_list[i + 1]) % 5 == 0:
                total_list.append(numbers_list[i] + numbers_list[i + 1])
print(len(total_list), max(total_list))
