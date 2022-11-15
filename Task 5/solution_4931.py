n_max = -float("inf")
for i in range(13, 1000):
    n = i
    i = bin(i)[2::]
    if n % 2 == 0:
        i += bin(i.count("1"))[2::]
    else:
        i = "1" + i + "00"
    if int(i, 2) < 1000 and n > n_max:
        n_max = n
print(n_max)
