with open("Files/4217", "r") as f:
    abc = f.readline().strip()
    total_list = []
    count = 0
    cond = True
    for i in range(len(abc) - 1):
        if abc[i] == "Q" and abc[i + 1] == "W":
            count += 1
            total_list.append(count)
            count = 1
            cond = False
        elif abc[i] == "W" and cond is False:
            cond = True
        else:
            count += 1
print(max(total_list))
