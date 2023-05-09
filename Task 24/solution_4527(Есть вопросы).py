with open("Files/4527", "r") as f:
    abc = f.readline().strip()
    total_list = []
    count = [0, 0, 0, 0, 0]
    number_dot = 1
    for i in range(len(abc)):
        if abc[i] == ".":
            if number_dot == 0:
                total_list.append(count[0])
                count[0] = 0
                number_dot = 1
            elif number_dot == 1:
                total_list.append(count[1])
                count[1] = 0
                number_dot += 1
            elif number_dot == 2:
                total_list.append(count[2])
                count[2] = 0
                number_dot += 1
            elif number_dot == 3:
                total_list.append(count[3])
                count[3] = 0
                number_dot += 1
            elif number_dot == 4:
                total_list.append(count[4])
                count[4] = 0
                number_dot = 0
        else:
            count[0] = count[0] + 1
            count[1] = count[1] + 1
            count[2] = count[2] + 1
            count[3] = count[3] + 1
            count[4] = count[4] + 1
print(max(total_list))
