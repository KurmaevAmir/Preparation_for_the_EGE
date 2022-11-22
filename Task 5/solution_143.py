for i in range(10000, 100000):
    i = str(i)
    arr = []
    arr.append(int(i[0]) + int(i[2]) + int(i[4]))
    arr.append(int(i[1]) + int(i[3]))
    arr.sort()
    number = int(str(arr[0]) + str(arr[1]))
    if number == 723:
        print(i)
        break
