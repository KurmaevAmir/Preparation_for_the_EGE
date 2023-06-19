with open("Files/26(2).txt", "r") as f:
    k = int(f.readline().strip())
    n = int(f.readline().strip())
    input_list = []
    for i in range(n):
        number1, number2 = [int(i) for i in f.readline().strip().split()]
        input_list.append([number1, number2])
    input_list.sort()
    container_list = [0] * k
    container_time = [0] * k
    count = 0
    for i in range(n):
        for j in range(k):
            if container_list[j] <= input_list[i][0]:
                container_list[j] = input_list[i][1] + 1
                count += 1
                container_time[j] = container_time[j] + input_list[i][1] - input_list[i][0]
                break
    print(count, container_time.index(max(container_time)) + 1)
