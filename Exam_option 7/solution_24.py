with open("Files/24.txt", "r") as f:
    abc = f.read().strip()
    count = 1
    total_list = []
    for i in range(len(abc) - 1):
        if abc[i] == abc[i + 1] and abc[i] not in ["X", "Y", "Z"]:
            count += 1
        elif count != 1:
            total_list.append(count)
            count = 1
print(max(total_list))
