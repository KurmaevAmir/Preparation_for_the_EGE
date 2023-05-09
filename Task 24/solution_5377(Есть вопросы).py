with open("Files/5377", "r") as f:
    abc = f.readline().strip()
    total_list = []
    count = 0
    cond = False
    for i in range(0, len(abc) - 2, 3):
        if abc[i] == "N" and abc[i + 1] == "P" and abc[i + 2] == "O":
            count += 1
        elif abc[i] == "P" and abc[i + 1] == "N" and abc[i + 2] == "O":
            count += 1
        elif count != 0:
            total_list.append(count)
            count = 0
print(max(total_list))
