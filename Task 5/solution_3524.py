total_list = []
for i in range(13, 55):
    remainder_list = []
    while i // 6 > 0:
        remainder_list.append(i % 6)
        i //= 6
    remainder_list.append(i % 6)
    remainder_list = remainder_list[::-1]
    remainder_list.append(remainder_list[-1])
    remainder_list = [str(j) for j in remainder_list]
    n = int("".join(remainder_list), 6)
    n_bin = bin(n)[2:]
    n_bin += n_bin[-1]
    n = int(n_bin, 2)
    if n < 344:
        total_list.append(n)
print(total_list[-1])
