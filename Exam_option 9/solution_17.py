with open("Files/17.txt", "r") as f:
    input_list = [int(i) for i in f.read().strip().split()]
    total_list = []
    for i in range(len(input_list) - 1):
        for j in range(i + 1, len(input_list)):
            if (input_list[i] + input_list[j]) % 7 == 0:
                total_list.append(input_list[i] + input_list[j])
print(len(total_list), max(total_list))
