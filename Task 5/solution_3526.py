total_list = []
for i in range(256):
    bin_n = bin(i)[2:]
    bin_n_reversed = bin_n[::-1]
    n = int(bin_n, 2)
    n_reversed = int(bin_n_reversed, 2)
    total_list.append(n - n_reversed)
print(max(total_list))
