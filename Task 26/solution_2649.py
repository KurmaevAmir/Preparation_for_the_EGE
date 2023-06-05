import math

with open("Files/2649", "r") as f:
    n = int(f.readline().strip())
    mass = []
    not_in_stock = []
    for i in range(n):
        number = int(f.readline().strip())
        if number <= 150:
            not_in_stock.append(number)
        else:
            mass.append(number)
    mass.sort()
    second_items = mass[:len(mass) // 2]
    print(second_items[-1])
    sum_discount = 0
    print(math.ceil(sum(second_items) - sum(second_items) * 0.2) + sum(not_in_stock) + sum(mass[len(mass) // 2:]))
