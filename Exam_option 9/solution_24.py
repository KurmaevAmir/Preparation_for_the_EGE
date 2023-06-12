with open("Files/24.txt", "r") as f:
    input_string = f.read().strip()
    max_len = -float("inf")
    count = 1
    for i in range(len(input_string) - 1):
        if input_string[i] == input_string[i + 1] == "D":
            count += 1
        elif count != 0:
            max_len = max(max_len, count)
            count = 1
print(max_len)
