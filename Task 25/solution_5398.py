def insert_number(start, stop, mass, number):
    count_insert = 0
    for i in range(stop):
        del mass[i]
        mass.insert(i, str(number)[count_insert])
        count_insert += 1
    return mass


x = [""]
count_x = 0
count = 0
count_digit = 1
while count != 5:
    mask = f"12345{''.join(x)}76"
    if int(mask) % 73 == 0:
        print(mask, int(mask) // 73)
        count += 1
    if "".join(x)[count_digit - 1:len(str(count_x))] == "9" * count_digit:
        x.insert(0, "0")
        count_digit += 1
        count_x = 0
    if x == [""]:
        x = ["0"]
        count_x = -1
    elif count_x == 10 ** (count_digit - 1) and count_digit > 1:
        x = insert_number(count_digit - 2, len(x), x, count_x)
    else:
        x = insert_number(count_digit - 1, len(x), x, count_x)
    count_x += 1
