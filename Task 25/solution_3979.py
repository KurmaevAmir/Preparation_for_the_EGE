total_list = []
for m in range(0, 30, 2):
    for n in range(1, 30, 2):
        number = (2 ** m) * (5 ** n)
        if 100000000 <= number <= 300000000:
            total_list.append((number, m + n))
total_list.sort(key=lambda x: x[0])
for elem in total_list:
    print(elem)
