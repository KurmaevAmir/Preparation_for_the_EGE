with open("Files/4517", "r") as f:
    n, m = [int(i) for i in f.readline().strip().split()]
    mass = []
    for i in range(n):
        number, letter = [i for i in f.readline().strip().split()]
        mass.append((int(number), letter))
    mass.sort()
    basket = 0
    letters_list = []
    for i in range(n):
        if mass[i][0] + basket > m:
            break
        basket += mass[i][0]
        letters_list.append(mass[i][1])
    l = len(letters_list)
    difference = m - basket
    for i in range(l - 1, - 1, - 1):
        if letters_list[i] == "Q" and difference > 0:
            for j in range(l, n):
                if mass[j][0] - mass[i][0] < difference and mass[j][1] == "Z":
                    l = j + 1
                    basket += (mass[j][0] - mass[i][0])
                    difference = m - basket
                    letters_list[i] = mass[j][1]
                    break
    print(letters_list.count("Z"), m - basket)
