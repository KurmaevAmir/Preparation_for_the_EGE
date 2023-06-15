def function(file):
    with open(f"Input_files_27990/{file}", "r") as f:
        n = int(f.readline().strip())
        multiples62 = 0
        multiples31 = 0
        multiples2 = 0
        other = 0
        for i in range(n):
            number = int(f.readline().strip())
            if number % 62 == 0:
                multiples62 += 1
            elif number % 31 == 0:
                multiples31 += 1
            elif number % 2 == 0:
                multiples2 += 1
            else:
                other += 1
        total = multiples62 * other + multiples62 * (multiples31 + multiples2) \
                + (multiples62 * (multiples62 - 1)) // 2 + multiples2 * multiples31
        return total


print(function("27990_A.txt"))
print(function("27990_B.txt"))
