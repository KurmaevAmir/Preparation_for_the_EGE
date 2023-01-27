def change_base_to_seven(number):
    remainder_list = []
    while number // 7 > 0:
        remainder_list.append(str(number % 7))
        number //= 7
    remainder_list.append(str(number))
    return "".join((remainder_list[::-1]))


n = ((7 ** 80 - 7 ** 4 + 123) // 3) * 20
n = change_base_to_seven(n)
print(n.count("4"))
