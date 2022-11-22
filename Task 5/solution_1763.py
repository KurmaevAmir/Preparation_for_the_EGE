total_list = []
for i in range(501):
    n_bin = bin(i)[2:]
    n = int(n_bin[::-1], 2)
    if n == 13:
        total_list.append(i)
print(total_list[-1])
