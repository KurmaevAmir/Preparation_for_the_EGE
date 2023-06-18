with open("Files/17.txt", "r") as f:
    input_list = [int(i) for i in f.read().strip().split()]
    total_list = []
    max_number = -float("inf")
    for i in range(len(input_list)):
        if len(str(input_list[i])) == 2:
            max_number = max(max_number, input_list[i])
    for i in range(len(input_list) - 1):
        if len(str(input_list[i])) == 2 and len(str(input_list[i + 1])) != 2 and \
                (input_list[i] + input_list[i + 1]) % max_number == 0:
            total_list.append((input_list[i] + input_list[i + 1]))
        elif len(str(input_list[i + 1])) == 2 and len(str(input_list[i])) != 2 and \
                (input_list[i] + input_list[i + 1]) % max_number == 0:
            total_list.append((input_list[i] + input_list[i + 1]))
print(len(total_list), max(total_list))
