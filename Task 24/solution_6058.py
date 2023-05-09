with open("Files/6058", "r") as f:
    abc = f.readline().strip()
    total_list = []
    while abc != "":
        count = 1
        max_count = -float('inf')
        letter = ""
        for i in range(len(abc) - 1):
            if abc[i] == abc[i + 1]:
                count += 1
            elif count != 1:
                if max_count != max(max_count, count):
                    max_count = count
                    letter = abc[i - 1]
                count = 1
        total_list.append((max_count, abc.count(letter)))
        abc = f.readline().strip()
total_list.sort(reverse=True, key=lambda x: x[0])
print(total_list)
# 29
