count = 0
for i in range(103, 10 ** 9 + 1, 103):
    if i % 103 == 0:
        number = str(i)
        cond = True
        for j in range(len(number) - 1):
            if ord(number[j]) >= ord(number[j + 1]):
                cond = False
                break
        if cond:
            count += 1
            print(i, i // 103)
            if count == 5:
                break
