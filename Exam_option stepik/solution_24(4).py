with open("Files/24(4)", "r") as f:
    input_string = f.readline().strip()
    max_len = 1
    count = 1
    input_string = input_string.replace("A", "!")
    input_string = input_string.replace("B", "!")
    input_string = input_string.replace("C", "!")
    for i in range(len(input_string) - 1):
        if input_string[i] + input_string[i + 1] != "!!":
            count += 1
            max_len = max(max_len, count)
        else:
            count = 1
print(max_len)
