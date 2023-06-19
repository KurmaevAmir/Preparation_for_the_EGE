# with open("Files/4933", "r") as f:
#     n = int(f.readline().strip())
#     mass = []
#     for i in range(n):
#         mass.append([int(i) for i in f.readline().strip().split()])
#     mass.sort()
#     count = 1
#     total_list = []
#     time = 0
#     time_start = 0
#     time_finish = 0
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             if mass[i][1] <= mass[j][0]:
#                 break
#             count += 1
#         total_list.append(count)
#         if count == 1:
#             time += mass[i][1] - mass[i][0]
#             time_finish = 0
#             time_start = 0
#         elif time_finish == 0:
#             time_start = mass[i][0]
#         count = 1
#     print(max(total_list))

with open("Files/4933", "r") as f:
    N = int(f.readline().strip())
    b = []
    for i in range(N):
        a = f.readline().strip().split(' ')
        b.append((int(a[0]), int(a[1])))
    b.sort()
    a = [0] * 1000000
    for i in range(N):
        a[b[i][0]] += 1
        a[b[i][1]] -= 1

    k = 0
    m = 0
    count = 0
    for i in range(1000000):
        k +=a[i]
        m = max(m, k)
        if k > 0:
            count += 1
print(m, count)
