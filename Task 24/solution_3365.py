with open("Files/3365", "r") as f:
    symbols = f.readline().strip()
    total_list = []
    abc = ""
    for i in range(len(symbols) - 1):
        if ord(symbols[i]) < ord(symbols[i + 1]):
            abc += symbols[i]
        elif abc != "":
            abc += symbols[i]
            total_list.append((abc, len(abc)))
            abc = ""
total_list.sort(reverse=True, key=lambda x: x[1])
print(total_list[0])
