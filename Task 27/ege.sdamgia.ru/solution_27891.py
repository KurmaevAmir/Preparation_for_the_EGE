def analyze_file(file):
    with open(file, "r") as f:
        n = int(f.readline())
        f_sum = 0
        max_n14 = 0
        max_n = 0
        for i in range(n):
            number = int(f.readline())
            if number % 14 == 0:
                max_n14 = max(max_n14, number)
            max_n = max(max_n, number)
        print(max_n * max_n14)


analyze_file("Input_files_27891/27-A_2.txt")
analyze_file("Input_files_27891/27-B_2.txt")
