total_list = []
for i in range(20, 601):
    n_bin = (bin(i)[2:-2])
    n = int(n_bin, 2)
    if n not in total_list:
        total_list.append(n)
print(len(total_list))
