with open("Files/4919", "r") as f:
    abc = f.readline().strip()
    count = 0
    for i in range(len(abc)):
        if abc[i] == "A":
            count_f = 0
            substring_length = 1
            for j in range(i + 1, len(abc)):
                if abc[j] == "F":
                    count_f += 1
                    if count_f == 3:
                        break
                elif abc[j] == "B":
                    substring_length += 1
                    if count_f == 2 and substring_length >= 20:
                        count += 1
                    else:
                        break
                elif abc[j] == "A":
                    break
                else:
                    substring_length += 1
print(count)
