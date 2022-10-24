def analyze_file(file):
    with open(file, "r") as f:
        n = int(f.readline())
        min_difference = float("inf")
        f_sum = 0
        for i in range(n):
            s = [int(j) for j in f.readline().split()]
            max_s = max(s)
            f_sum += max_s
            if abs(s[0] - s[1]) % 5 != 0:
                min_difference = min(min_difference, abs(s[0] - s[1]))
        if f_sum % 5 != 0:
            print(f_sum)
        else:
            f_sum -= min_difference
            print(f_sum)


analyze_file("Input_files_27890/27-A_1.txt")
analyze_file("Input_files_27890/27-B_1.txt")
