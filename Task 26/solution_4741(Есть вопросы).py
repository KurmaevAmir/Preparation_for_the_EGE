with open("Files/4741", "r") as f:
    n, k = [int(i) for i in f.readline().strip().split()]
    mass = []
    for i in range(n):
        numbers = [int(i) for i in f.readline().strip().split()]
        if numbers != [0, 0]:
            mass.append(numbers)
    mass.sort()
    total_list = []
    for i in range(n - 1):
        for j in range(i + 1, n):

