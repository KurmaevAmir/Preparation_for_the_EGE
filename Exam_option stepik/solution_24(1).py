with open("Files/24(1)", "r") as f:
    input_string = f.readline().strip()
    vowels = ["A", "E"]
    consonants = ["B", "C", "D", "F"]
    count = 1
    total_list = []
    for i in range(len(input_string) - 1):
        if (input_string[i] in vowels and input_string[i + 1] in vowels) or \
                (input_string[i] in consonants and input_string[i + 1] in consonants):
            count += 1
        elif count != 1:
            total_list.append(count)
            count = 1
print(max(total_list))
