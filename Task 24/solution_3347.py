with open("Files/3347", 'r') as f:
    abc = f.readline().strip()
    total_list = []
    count = 1
    for i in range(len(abc) - 1):
        if abc[i] == abc[i + 1]:
            count += 1
        elif count != 1:
            total_list.append(count)
            count = 1
print(max(total_list))
