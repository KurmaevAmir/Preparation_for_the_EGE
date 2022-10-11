fibonacci_list = [1, 1]
count = 1
while fibonacci_list[-1] < 100:
    fibonacci_list.append(fibonacci_list[count - 1] + fibonacci_list[count])
    count += 1
del fibonacci_list[-1]
f = 1
f1 = 1
i = ""
intermediate_list = []
while i != 10:
    number = int(f'73{i}5{f}486{f1}')
    for f in fibonacci_list:
        for f1 in fibonacci_list:
            number = int(f'73{i}5{f}486{f1}')
            if number % 43 == 0:
                if number > 10 ** 9:
                    continue
                intermediate_list.append((number, number // 43))
    if i == "":
        i = 1
    else:
        i += 1
total_list = list(set(intermediate_list))
total_list.sort(key=lambda x: x[1])
for i in total_list:
    print(i[0], i[1])
