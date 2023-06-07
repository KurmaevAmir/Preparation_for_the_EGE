with open("Files/26.txt", "r") as f:
    n = int(f.readline().strip())
    input_massive = []
    count = 0
    for i in range(n):
        input_massive.append(int(f.readline().strip()))
    for i in range(n - 1):
        for j in range(i + 1, n):
            if input_massive[i] + input_massive[j] == 100:
                count += 1
                input_massive[i] = 0
                input_massive[j] = 0
print(count)
