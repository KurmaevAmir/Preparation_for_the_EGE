with open('Files/5071', "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    total_list = []
    for i in range(len(numbers_list) - 1):
        if abs(numbers_list[i] % 17 - numbers_list[i + 1] % 17) == (numbers_list[i] % 4 + numbers_list[i + 1] % 4):
            total_list.append(numbers_list[i] + numbers_list[i + 1])
print(len(total_list), min(total_list))
