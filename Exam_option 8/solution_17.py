with open("Files/17.txt", "r") as f:
    numbers_list = [int(i) for i in f.read().strip().split()]
    total_list = []
    for i in range(len(numbers_list) - 1):
        for j in range(i + 1, len(numbers_list)):
            if abs(numbers_list[i] - numbers_list[j]) % 36 == 0 and \
                    (numbers_list[i] % 13 == 0 or numbers_list[j] % 13 == 0):
                total_list.append(abs(numbers_list[i] - numbers_list[j]))
print(len(total_list), max(total_list))
