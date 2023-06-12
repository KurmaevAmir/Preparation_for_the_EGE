with open("Files/5379", "r") as f:
    n = int(f.readline().strip())
    input_mass = []
    for i in range(n):
        input_mass.append(int(f.readline().strip()))
    input_mass.sort()
    number_of_items_on_sale = n // 4 - 1
    valid_check = 0
    estimated_check = 0
    for i in range(n):
        if i <= number_of_items_on_sale:
            valid_check += input_mass[i] * 0.5
        else:
            valid_check += input_mass[i]
    input_mass.sort(reverse=True)
    for i in range(n):
        if i <= number_of_items_on_sale:
            estimated_check += input_mass[i] * 0.5
        else:
            estimated_check += input_mass[i]
print(int(estimated_check), int(valid_check))
