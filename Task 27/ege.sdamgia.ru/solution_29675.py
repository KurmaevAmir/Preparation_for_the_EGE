def function(file):
    with open(f"Input_files_29675/{file}", "r") as f:
        n = int(f.readline().strip())
        difference_list = []
        f_sum = 0
        for i in range(n):
            numbers_list = [int(i) for i in f.readline().strip().split()]
            f_sum += max(numbers_list)
            if abs(numbers_list[0] - numbers_list[1]) % 3 != 0:
                difference_list.append(abs(numbers_list[0] - numbers_list[1]))
        difference_list.sort()
        i = 0
        f_sum2 = f_sum
        while f_sum % 3 != 0:
            if (f_sum - difference_list[i]) % 3 == 0:
                f_sum -= difference_list[i]
                print(f_sum)
                break
            f_sum2 -= difference_list[i]
            if f_sum2 % 3 == 0:
                print(f_sum2)
                break
            i += 1


function("inf_22_10_20_27a.txt")
function("inf_22_10_20_27b.txt")
