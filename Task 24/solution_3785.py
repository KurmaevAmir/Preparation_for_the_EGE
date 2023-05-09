alphabet_list = ["A", "B", "C", "D", "E", "F", "G",
                 "H", "I", "J", "K", "L", "M", "N",
                 "O", "P", "Q", "R", "S", "T", "U",
                 "V", "W", "X", "Y", "Z"]
with open("Files/3785", "r") as f:
    file_list = []
    abc = f.readline().strip()
    file_list.append(abc)
    total_list = []
    while abc != "":
        count = 1
        max_count = -float("inf")
        for i in range(len(abc) - 1):
            if abc[i] == abc[i + 1]:
                count += 1
            elif count != 1:
                max_count = max(max_count, count)
                count = 1
        letter = ""
        min_count_letter = float("inf")
        for i in alphabet_list:
            if abc.count(i) != 0 and abc.count(i) < min_count_letter:
                letter = i
                min_count_letter = abc.count(i)
            elif abc.count(i) == min_count_letter:
                letter = max(i, letter)
        total_list.append((max_count, letter))
        abc = f.readline().strip()
        file_list.append(abc)
file_symbols = "".join(file_list)
total_list.sort(reverse=True, key=lambda x: x[0])
print(f'{total_list[0][1]}{file_symbols.count(total_list[0][1])}')
