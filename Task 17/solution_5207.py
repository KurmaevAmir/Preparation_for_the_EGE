with open("Files/5207", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    average = sum(numbers_list) / len(numbers_list)
    total_list = []
    for i in range(len(numbers_list) - 2):
        if (int(str(numbers_list[i])[0]) + int(str(numbers_list[i + 1])[0]) == int(str(numbers_list[i])[-1]) + int(str(numbers_list[i + 1])[-1]) and numbers_list[i] != numbers_list[i + 1]) or\
            (int(str(numbers_list[i + 2])[0]) + int(str(numbers_list[i + 1])[0]) == int(str(numbers_list[i + 2])[-1]) + int(str(numbers_list[i + 1])[-1]) and numbers_list[i + 1] != numbers_list[i + 2]) or\
                (int(str(numbers_list[i])[0]) + int(str(numbers_list[i + 2])[0]) == int(str(numbers_list[i])[-1]) + int(str(numbers_list[i + 2])[-1]) and numbers_list[i] != numbers_list[i + 2]):
            if (numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2]) / 3 > average:
                total_list.append(numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2])
print(len(total_list), max(total_list))
