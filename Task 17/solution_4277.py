with open("Files/4277", "r") as f:
    max_len = 0
    sequences_list = []
    current_len = 1
    numbers_list = [int(i) for i in f.read().split()]
    for i in range(len(numbers_list) - 1):
        if numbers_list[i] > numbers_list[i + 1]:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            sequences_list.append(current_len)
            current_len = 1
print(max_len, sequences_list.count(max_len))
