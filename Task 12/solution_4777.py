for i in range(401, 500):
    n = i * "5"
    while "5555" in n:
        n = n.replace("5555", "8", 1)
        n = n.replace("88", "5", 1)
    print(i, n.count("5"))