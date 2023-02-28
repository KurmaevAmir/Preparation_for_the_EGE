with open('Files/4321', "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    total_list = []
    for number in numbers_list:
        if number % 5 == 3 and number % 9 == 5 and number % 8 != 7:
            total_list.append(number)
print(len(total_list), max(total_list))
