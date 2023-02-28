with open("Files/5251", "r") as f:
    numbers_list = [int(i) for i in f.read().split()]
    sum_numbers = 0
    for number in numbers_list:
        if number % 22 == 0:
            sum_numbers += sum([int(i) for i in str(number)])
    total_list = []
    for i in range(len(numbers_list) - 2):
        pair = numbers_list[i] + numbers_list[i + 1]
        pair2 = numbers_list[i + 1] + numbers_list[i + 2]
        pair3 = numbers_list[i] + numbers_list[i + 2]
        cond1 = True
        for j in (oct(pair)[2:]):
            if int(j) % 2 != 0:
                cond1 = False
                break
        cond2 = True
        for j in (oct(pair2)[2:]):
            if int(j) % 2 != 0:
                cond2 = False
                break
        cond3 = True
        for j in (oct(pair3)[2:]):
            if int(j) % 2 != 0:
                cond3 = False
                break
        if cond1 and cond2 and cond3:
            if numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2] < sum_numbers:
                total_list.append(numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2])
            continue
print(len(total_list), min(total_list))
