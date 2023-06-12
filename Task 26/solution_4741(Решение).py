with open("Files/4741", "r") as f:
    n, k = [int(i) for i in f.readline().strip().split()]
    mass = []
    count = 0
    max_count = 0
    max_time = 0
    start_time = k
    end_time = k + 24 * 3600000
    time_process = [0 for i in range(24 * 3600000 + 1)]
    print(len(time_process))
    for i in f:
        start_process, end_process = [int(j) for j in i.strip().split()]
        if (start_process < start_time) and ((end_process > start_time) or (end_process == 0)):
            count = count + 1
        if (start_process >= start_time) and (start_process <= end_time):
            time_process[start_process - start_time] = time_process[start_process - start_time] + 1
        if (end_process >= start_time) and (int(end_process) <= end_time):
            time_process[end_process - start_time] = time_process[end_process - start_time] - 1
    sum_time = 0
    max_process = 0
    for i in range(1, 24 * 3600000):
        count = count + time_process[i]
        if count > max_process:
            max_process = count
            sum_time = 0
        if count == max_process:
            sum_time = sum_time + 1
    print(max_process, sum_time)
