def function(file):
    with open(f"Input_files_28130/{file}", "r") as f:
        n = int(f.readline().strip())
        mass = []
        for i in range(n):
            mass.append(int(f.readline().strip()))
        m = 80
        b = 50
        count = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (mass[i] + mass[j]) % m == 0 and (mass[i] > b or mass[j] > b):
                    count += 1
    return count


print(function("28130_A.txt"))
print(function("28130_B.txt"))
