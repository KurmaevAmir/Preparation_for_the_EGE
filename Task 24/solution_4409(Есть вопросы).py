from re import fullmatch

with open("Files/4409", "r") as f:
    abc = f.readline().strip()
    pattern = r'CB[^A, B, F]{1}BC'
    alphabet_dictionary = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0,
                           "F": 0, "G": 0, "H": 0, "I": 0, "J": 0,
                           "K": 0, "L": 0, "M": 0, "N": 0, "O": 0,
                           "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0,
                           "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0,
                           "Z": 0}
    for i in range(len(abc) - 2):
        if fullmatch(pattern, abc[i:i + 5]):
            alphabet_dictionary[abc[i + 2]] = alphabet_dictionary[abc[i + 2]] + 1
    count = 0
    for i in range(len(abc) - 5):
        if abc[i:i+5] == "CBCBC":
            count += 1
    print(count)
print(alphabet_dictionary)
