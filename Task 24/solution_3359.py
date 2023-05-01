with open("Files/3359", "r") as f:
    abc = f.readline().strip()
    count = 1
    total_list = []
    for i in range(len(abc) - 1):
        if ord(abc[i]) > ord(abc[i + 1]):
            count += 1
        elif count != 1:
            total_list.append(count)
            count = 1
print(max(total_list))
