massive = []
for m in range(0, 30, 2):
    for n in range(1, 30, 2):
        a = (2 ** m) * (7 ** n)
        if 100000000 <= a <= 300000000:
            massive.append((a, m + n))
massive.sort()
for i in massive:
    print(i[0], i[1])
