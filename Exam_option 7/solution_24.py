with open("Files/24.txt", "r") as f:
    abc = f.read().strip()
    count = 1
    total_list = []
    for i in range(len(abc) - 1):
        if not(abc[i] in ["X", "Y", "Z"] and abc[i + 1] in ["X", "Y", "Z"]):
            count += 1
        elif count != 1:
            total_list.append(count)
            count = 1
total_list.append(count)
print(max(total_list))
