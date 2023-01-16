for i in range(2, 11):
    n1 = 1 * i + 2
    n2 = 3 * i + 1
    n3 = 4 * i ** 2 + 2
    if n1 * n2 == n3:
        print(i)
        break
