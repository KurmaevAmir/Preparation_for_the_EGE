for i in range(1, 10000000):
    n = i
    s1 = sum([int(j) for j in str(i) if int(j) % 2 == 0])
    n_reversed = str(i)[::-1]
    s2 = sum([int(n_reversed[j]) for j in range(len(str(i))) if j % 2 == 0])
    r = abs(s1 - s2)
    if r == 26:
        print(n)
        break
