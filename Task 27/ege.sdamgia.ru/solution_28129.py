def analyze_file(file):
    with open(file, "r") as f:
        n = int(f.readline())
        num1_main = 0
        num2_main = 0
        for i in range(n):
            number = int(f.readline())
            if number % 7 == 0:
                if number % 160 != num2_main % 160:
                    num1_main = max(number, num1_main)
            else:
                if number % 160 != num1_main % 160:
                    num2_main = max(number, num2_main)
    print(num1_main, num2_main)


analyze_file("Input_files_28129/28129_A.txt")
analyze_file("Input_files_28129/28129_B.txt")
