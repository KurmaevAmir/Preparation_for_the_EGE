max_n = -float('inf')
for i in range(1000):
    n = bin(i)[2:]
    if i % 2 == 0:
        n += bin(n.count("1"))[2:]
    else:
        n = "1" + n + "00"
    if int(n, 2) < 1000:
        max_n = max(i, max_n)
print(max_n)
