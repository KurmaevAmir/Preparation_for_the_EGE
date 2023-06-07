with open("Files/24.txt", "r") as f:
    symbols_list = f.readline().strip()
    symbols_list = symbols_list.replace("AA", "!")
    symbols_list = symbols_list.replace("CC", "?")
    total_list = []
    count = 0
    for i in range(len(symbols_list)):
        if symbols_list[i] == "!" or symbols_list[i] == "?":
            count += 1
        elif count != 0:
            total_list.append(count)
            count = 0
print(max(total_list))
