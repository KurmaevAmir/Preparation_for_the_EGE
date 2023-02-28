with open("Files/4315", "r") as f:
    numbers_list = [i for i in f.read().split()]
    total_list = []
    for number in numbers_list:
        if int(number) > 100:
            if int(number[-2]) <= 4 and 3 <= int(number[-3]) <= 7:
                total_list.append(number)
print(len(total_list), min(total_list))
