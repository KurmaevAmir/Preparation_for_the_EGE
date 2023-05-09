alphabet_list = ["A", "B", "C", "D", "E", "F", "G",
                 "H", "I", "J", "K", "L", "M", "N",
                 "O", "P", "Q", "R", "S", "T", "U",
                 "V", "W", "X", "Y", "Z"]
with open("Files/3783", "r") as f:
    file_list = []
    abc = f.readline().strip()
    file_list.append(abc)
    total_list = []
    while abc != "":
        count = 0
        for i in range(len(abc) - 1):
            if ord(abc[i]) + 1 == ord(abc[i + 1]):
                count += 1
        letter = ""
        max_count_letter = -float('inf')
        for i in alphabet_list:
            if max_count_letter < abc.count(i):
                letter = i
                max_count_letter = abc.count(i)
            elif max_count_letter == abc.count(i):
                letter = max(i, letter)
        total_list.append((count, max_count_letter, letter))
        abc = f.readline().strip()
        file_list.append(abc)
file_symbols = "".join(file_list)
total_list.sort(key=lambda x: x[0])
print(f'{total_list[0][2]}{file_symbols.count(total_list[0][2])}')
