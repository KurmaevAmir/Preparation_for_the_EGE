n = bin(151)[2:]
n = str(int(len(n) * "1") - int(n))
while len(n) < 8:
    n = "0" + n
n_part1 = n[:4]
n_part2 = n[4:]
print(str(int(n_part1, 2)) + str(int(n_part2, 2)))
