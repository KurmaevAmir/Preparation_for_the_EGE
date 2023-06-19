with open("Files/26(2).txt", "r") as f:
    k = int(f.readline().strip())
    n = int(f.readline().strip())
    input_list = []
    for i in range(n):
        number1, number2 = [int(i) for i in f.readline().strip().split()]
        input_list.append([number1, number2])
    input_list.sort()
    container_list = [0] * k
    container_minute = [0] * 1445
    count = 0
    for i in range(n):
        for j in range(k):
            if container_list[j] <= input_list[i][0]:
                container_list[j] = input_list[i][1] + 1
                count += 1
                for l in range(input_list[i][0], input_list[i][1]):
                    container_minute[l] += 1
                break
    max_time = max(container_minute)
    pos = 0
    for i in range(len(container_minute)):
        if container_minute[i] == max_time:
            pos = i
    print(count, pos)
