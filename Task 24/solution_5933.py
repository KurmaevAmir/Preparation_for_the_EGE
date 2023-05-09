with open("Files/5933", "r") as f:
    abc = f.readline().strip()
    total_list = []
    for i in range(len(abc) - 1):
        if abc[i] == "D" and (abc[i + 1] == "A" or abc[i + 1] == "D"):
            d_count = 0
            if abc[i + 1] == "D":
                d_count = 1
            count = 1
            for j in range(i + 1, len(abc)):
                if abc[j] == "A" and d_count == 0:
                    count += 1
                    d_count += 2
                elif abc[j] == "D" and d_count > 0:
                    count += 1
                    d_count -= 1
                else:
                    total_list.append(count)
                    break
        elif abc[i] == "A" and abc[i + 1] == "D":
            count = 1
            d_count = 2
            for j in range(i + 1, len(abc)):
                if abc[j] == "A" and d_count == 0:
                    count += 1
                    d_count += 2
                elif abc[j] == "D" and d_count > 0:
                    count += 1
                    d_count -= 1
                else:
                    total_list.append(count)
                    break
print(max(total_list))
