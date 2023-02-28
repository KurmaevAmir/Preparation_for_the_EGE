with open("Files/4313", "r") as f:
    true_numbers_list = []
    numbers_list = [int(i) for i in f.read().split()]
    for number in numbers_list:
        if bin(number)[-4:] == "1001":
            remainders_list = []
            number_five = number
            for i in range(2):
                remainders_list.append(number_five % 5)
                number_five //= 5
            if remainders_list == [1, 1]:
                true_numbers_list.append(number)
print(max(true_numbers_list), sum(true_numbers_list))
