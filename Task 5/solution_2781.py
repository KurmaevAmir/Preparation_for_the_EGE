for i in range(255):
    n_bin = bin(i)[2:]
    n_reversed = str(11111111 - int(n_bin))
    if int(n_reversed, 2) + 1 == 221:
        print(i)
