discount_dict = {"A": [0, 0], "B": [0, 0], "AC": [0.1, 1], "BC": [0.2, 1]}
with open("Files/5935", "r") as f:
    n, s = [int(i) for i in f.readline().strip().split()]
    input_mass = []
    for i in range(n):
        number, letter = [i for i in f.readline().strip().split()]
        number = int(number) - int(number) * discount_dict[letter][0]
        input_mass.append([number, discount_dict[letter][1]])
    input_mass.sort()
    count = 0
    basket = 0
    max_number = 0
    for i in range(n):
        if basket + input_mass[i][0] > s:
            break
        if input_mass[i][1] == 1:
            max_number = input_mass[i][0]
        basket += input_mass[i][0]
        count += 1
    difference = s - basket
    for i in range(count, n):
        if input_mass[i][0] - input_mass[count - 1][0] <= difference and \
                input_mass[i][1] == 1:
            max_number = input_mass[i][0]
    print(int(round(basket, 0)), int(round(max_number, 0)))
