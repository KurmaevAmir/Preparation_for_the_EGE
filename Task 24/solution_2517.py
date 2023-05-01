with open("Files/2517", "r") as f:
    abc = f.readline().strip()
    len_abc_list = []
    count = 0
    for i in abc:
        if i in ["A", "B", "E", "F"]:
            count += 1
        elif count != 0:
            len_abc_list.append(count)
            count = 0
print(max(len_abc_list))
