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
        cond = True
        for j in (oct(pair)[2:]):
            if int(j) % 2 != 0:
                cond = False
                break
        if cond:
            if sum([int(j) for j in str(numbers_list[i])]) + sum([int(j) for j in str(numbers_list[i + 1])]) + sum([int(j) for j in str(numbers_list[i + 2])]) < sum_numbers:
                total_list.append(numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2])
            continue
        cond = True
        for j in (oct(pair2)[2:]):
            if int(j) % 2 != 0:
                cond = False
                break
        if cond:
            if sum([int(j) for j in str(numbers_list[i])]) + sum([int(j) for j in str(numbers_list[i + 1])]) + sum([int(j) for j in str(numbers_list[i + 2])]) < sum_numbers:
                total_list.append(numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2])
            continue
        cond = True
        for j in (oct(pair3)[2:]):
            if int(j) % 2 != 0:
                cond = False
                break
        if cond:
            if sum([int(j) for j in str(numbers_list[i])]) + sum([int(j) for j in str(numbers_list[i + 1])]) + sum([int(j) for j in str(numbers_list[i + 2])]) < sum_numbers:
                total_list.append(numbers_list[i] + numbers_list[i + 1] + numbers_list[i + 2])
            continue
print(len(total_list), min(total_list))
