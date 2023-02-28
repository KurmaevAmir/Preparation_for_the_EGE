with open("Files/5191", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    average = sum(numbers_list) / len(numbers_list)
    total_list = []
    for i in range(len(numbers_list) - 1):
        if "101010" in bin(numbers_list[i] * numbers_list[i + 1]) and numbers_list[i] + numbers_list[i + 1] > average:
            total_list.append(numbers_list[i] + numbers_list[i + 1])
print(len(total_list), min(total_list))
