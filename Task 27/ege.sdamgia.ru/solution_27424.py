def reading_file(file):
    with open(f"{file}", "r") as f1:
        n = int(f1.readline())
        min_difference = float("inf")
        f1_sum = 0
        for i in range(n):
            s = [int(j) for j in f1.readline().split()]
            max_s = max(s)
            f1_sum += max_s
            if abs(s[0] - s[1]) % 3 != 0:
                min_difference = min(min_difference, abs(s[0] - s[1]))
        if f1_sum % 3 != 0:
            print(f1_sum)
        else:
            f1_sum -= min_difference
            print(f1_sum)


reading_file("Input_files_27424/27-A_demo.txt")
reading_file("Input_files_27424/27-B_demo.txt")
