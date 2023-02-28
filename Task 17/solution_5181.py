with open("Files/5181", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    average = sum(numbers_list) / len(numbers_list)
    total_list = []
    for i in range(len(numbers_list) - 1):
        if (len(oct(numbers_list[i])[2:]) % 2 != 0 or len(oct(numbers_list[i + 1])[2:]) % 2 != 0) and numbers_list[i] + numbers_list[i + 1] > average:
            total_list.append(numbers_list[i] + numbers_list[i + 1])
print(len(total_list), min(total_list))
