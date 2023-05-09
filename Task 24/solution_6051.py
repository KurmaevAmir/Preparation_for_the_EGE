with open("Files/6051", "r") as f:
    abc = f.readline().strip()
    consonants_list = ["B", "C", "D", "F", "G", "H", "J",
                       "K", "L", "M", "N", "P", "Q", "R",
                       "S", "T", "V", "W", "X", "Z"]
    vowels_list = ["A", "E", "I", "O", "U", "Y"]
    count = 0
    count_consonants = 2
    total_list = []
    for i in range(len(abc)):
        if abc[i] in consonants_list and count_consonants == 2:
            count_consonants -= 1
        elif count_consonants == 1 and abc[i] in consonants_list:
            count_consonants -= 1
        elif count_consonants == 0 and abc[i] in vowels_list:
            count += 1
            count_consonants = 2
        elif count != 0:
            total_list.append(count)
            count = 0
            count_consonants = 2
total_list.append(count)
print(max(total_list))
