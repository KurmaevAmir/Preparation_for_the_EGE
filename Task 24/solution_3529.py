with open("Files/3529", "r") as f:
    abc = f.readline().strip()
    count = 0
    total_list = []
    cond = True
    for i in range(len(abc)):
        if abc[i] == "A":
            if cond:
                cond = False
                count += 1
            else:
                count = 1
        elif cond is False and abc[i] == "F":
            count += 1
            cond = True
            if count != 2:
                total_list.append(count)
            count = 0
        elif cond is False:
            count += 1
print(min(total_list))
