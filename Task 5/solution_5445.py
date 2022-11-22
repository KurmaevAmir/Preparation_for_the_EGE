for i in range(1234567891011122, 10000000000000000):
    n = str(i)
    n = n[::-1]
    n = [int(j) for j in n]
    n_copy = []
    for pos, elem in enumerate(n):
        if pos % 2 != 0:
            elem *= 2
            if elem // 10 > 0:
                elem = int(str(elem)[0]) + int(str(elem)[1])
        n_copy.append(elem)
    if sum(n_copy) % 10 == 0:
        print(str(i)[8:])
        break
