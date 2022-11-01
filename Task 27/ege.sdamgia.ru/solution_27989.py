def analyze_file(file):
    with open(file, "r") as f:
        n = int(f.readline())
        multiples26 = 0
        multiples13 = 0
        multiples2 = 0
        other = 0
        for i in range(n):
            number = int(f.readline())
            if number % 26 == 0:
                multiples26 += 1
            elif number % 13 == 0:
                multiples13 += 1
            elif number % 2 == 0:
                multiples2 += 1
            else:
                other += 1
        total = multiples26 * other + multiples26 * (multiples13 + multiples2)\
                + multiples13 * multiples2\
                + (multiples26 * (multiples26 - 1)) // 2
        print(total)


analyze_file("Input_files_27989/27989_A.txt")
analyze_file("Input_files_27989/27989_B.txt")
