with open("Files/24(3)", "r") as f:
    input_string = f.readline().strip()
    count = 1
    total_list = []
    for i in range(len(input_string) - 1):
        if ord(input_string[i]) > ord(input_string[i + 1]):
            count += 1
        elif count != 1:
            total_list.append(count)
            count = 1
total_list.append(count)
print(max(total_list))
