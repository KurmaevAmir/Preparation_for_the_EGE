with open("Files/6286", "r") as f:
    abc = f.readline().strip()
    total_list = []
    while abc != "":
        interim_list = []
        for i in range(len(abc) - 1):
            if abc[i] == "X":
                interim_list.append(abc[i + 1])
        for pos, elem in enumerate(interim_list):
            interim_list[pos] = (elem, interim_list.count(elem))
        interim_list.sort(reverse=True, key=lambda x: x[1])
        max_count = interim_list[0][1]
        for i in interim_list:
            if i[1] != max_count:
                break
            total_list.append(i[0])
        abc = f.readline().strip()
for pos, elem in enumerate(total_list):
    total_list[pos] = (elem, total_list.count(elem))
total_list.sort(reverse=True, key=lambda x: x[1])
print(total_list[0][1])
