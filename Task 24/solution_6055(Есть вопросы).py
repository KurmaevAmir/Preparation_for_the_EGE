with open("Files/6055", "r") as f:
    abc = f.readline().strip()
    count = 0
    total_list = []
    for i in range(len(abc)):
        if abc[i] == "F":
            count_e = 0
            for j in range(i + 1, len(abc)):
                if abc[j] == "E":
                    count_e += 1
                

