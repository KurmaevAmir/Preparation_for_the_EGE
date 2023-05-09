with open("Files/4041", "r") as f:
    abc = f.readline().strip()
    total_list = []
    while abc != "":
        max_count = -float("inf")
        if abc.count("G") <= 15:
            for i in range(len(abc)):
                letter = abc[i]
                count = 1
                for j in range(abc.index(letter) + 1, len(abc)):
                    if i != j:
                        count += 1
                    else:
                        max_count = max(max_count, count)
        abc = f.readline().strip()
        total_list.append(max_count)
print(max(total_list))
