def analyze_file(file):
    with open(file, "r") as f:
        n = int(f.readline())
        number2_17 = 0
        number2 = 0
        number1_17 = 0
        number1 = 0
        for i in range(n):
            number = int(f.readline())
            if number % 2 == 0:
                if number % 17 == 0:
                    number2_17 = max(number2_17, number)
                else:
                    number2 = max(number2, number)
            else:
                if number % 17 == 0:
                    number1_17 = max(number1_17, number)
                else:
                    number1 = max(number1, number)
    if number2_17 + number2 > number1_17 + number1:
        print(number2_17, number2)
    else:
        print(number1_17, number1)


analyze_file("Input_files_27991/27991_A.txt")
analyze_file("Input_files_27991/27991_B.txt")
