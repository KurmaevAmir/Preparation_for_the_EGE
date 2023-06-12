total_list = []
for i in range(10, 1001):
    i_bin = bin(i)[2:]
    i_bin = i_bin[1:]
    number = int(i_bin, 2)
    total_list.append(i - number)
total_list = set(total_list)
print(len(total_list))
