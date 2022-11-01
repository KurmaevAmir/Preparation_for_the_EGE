def analyze_file(file):
    with open(file, "r") as f:
        n = int(f.readline())
        max_n14 = 0
        max_n7 = 0
        max_n2 = 0
        max_n = 0
        for i in range(n):
            number = int(f.readline())
            if number % 14 == 0: #еще возможна ситуация, что наибольшим произведением окажется произведение чисел:
                # наибольшее, которое делится на 7, но не делится на 2 и наибольшее, которое делится на 2,
                # но не делится на 7. Еще вариант, что наибольшим окажется произведение двух наибольших чисел,
                # делящихся на 14.
                if (number >= max_n14) and (max_n14 >= max_n):
                    max_n, max_n14 = max_n14, number
                else:
                    max_n14 = max(max_n14, number)
            elif number % 7 == 0:
                max_n7 = max(max_n7, number)
                max_n = max(max_n7, max_n)
            elif number % 2 == 0:
                max_n2 = max(max_n2, number)
                max_n = max(max_n2, max_n)
            else:
                max_n = max(max_n, number)
        print(max((max_n * max_n14), (max_n2 * max_n7)))


analyze_file("Input_files_27891/27-A_2.txt")
analyze_file("Input_files_27891/27-B_2.txt")
