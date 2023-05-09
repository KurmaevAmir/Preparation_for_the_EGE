with open("Files/6182", "r") as f:
    abc = f.readline().strip()
    total_list = []
    for i in range(len(abc)):
        if abc[i] == "A":
            count = 1
            for j in range(i + 1, len(abc)):
                if abc[j] == "D":
                    count += 1
                    total_list.append(count)
                    break
                elif abc[j] == "A":
                    break
                count += 1
print(max(total_list))
