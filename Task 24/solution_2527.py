with open("Files/2527", "r") as f:
    abc = f.readline().strip()
    total_list = []
    abc_english_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                        "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                        "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in abc_english_list:
        abc = abc.replace(i, ";")
    abc = abc.split(";")
    abc = [i for i in abc if i != ""]
    for i in abc:
        cond = True
        for j in i:
            if int(j) % 2 == 0:
                cond = False
                break
        if cond:
            total_list.append(int(i))
print(max(total_list))
