with open("Files/4105", "r") as f:
    abc = f.readline().strip()
    abc_list = [1, 0, 0]
    count = 0
    total_list = []
    for i in range(len(abc) - 1):
        if abc[i] == abc[i + 1]:
            abc_list[count] += 1
        elif abc[i + 1] > abc[i]:
            count += 1
            if count <= 2:
                abc_list[count] += 1
            else:
                total_list.append(sum(abc_list))
                abc_list[0] = abc_list[1]
                abc_list[1] = abc_list[2]
                abc_list[2] = 0
                count = 2
                abc_list[count] += 1
        else:
            if count == 2:
                total_list.append(sum(abc_list))
                abc_list[0] = 1
                count = 0
                abc_list[1] = 0
                abc_list[2] = 0
    if count == 2:
        total_list.append(sum(abc_list))
print(max(total_list))
