def function(file):
    with open(file, "r") as f:
        n = int(f.readline().strip())
        input_mass = []
        for i in range(n):
            input_mass.append(int(f.readline().strip()))
        input_mass.sort()
        number0 = [i for i in input_mass if i % 3 == 0][-3:]
        number1 = [i for i in input_mass if i % 3 == 1][-3:]
        number2 = [i for i in input_mass if i % 3 == 2][-3:]
        return max(sum(number0), sum(number1), sum(number2),
                   max(number0) + max(number1) + max(number2))


print(function("Input_files_35485/27-A.txt"))
print(function("Input_files_35485/27-B.txt"))
