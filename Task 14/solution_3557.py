for i in range(2, 11):
    n1 = 1 * i ** 2 + 3
    n3 = 1 * (i + 1) ** 2 + 3
    if n1 + 11 == n3:
        print(i)
        break
