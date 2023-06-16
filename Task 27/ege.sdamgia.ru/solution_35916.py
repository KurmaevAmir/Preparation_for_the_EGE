def function(file):
    with open(file, "r") as f:
        n = int(f.readline().strip())
        input_mass = []
        for i in range(n):
            input_mass.append(int(f.readline().strip()))
        input_mass.sort(reverse=True)
        number0 = [i for i in input_mass if i % 3 == 0][-3:]
        number1 = [i for i in input_mass if i % 3 == 1][-3:]
        number2 = [i for i in input_mass if i % 3 == 2][-3:]
        return min(sum(number0), sum(number1), sum(number2),
                   min(number0) + min(number1) + min(number2))


print(function("Input_files_35916/27-A.txt"))
print(function("Input_files_35916/27-B.txt"))
