with open("Files/4695", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    max_number = -float('inf')
    for i in numbers_list:
        if i % 211 == 0:
            max_number = max(max_number, i)
    total_list = []
    for i in range(len(numbers_list) - 1):
        if numbers_list[i] > max_number or numbers_list[i + 1] > max_number:
            if "1" in str(numbers_list[i]) or "1" in str(numbers_list[i + 1]):
                total_list.append(numbers_list[i] + numbers_list[i + 1])
print(len(total_list), min(total_list))
