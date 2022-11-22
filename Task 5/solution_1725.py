total_list = []
for i in range(100, 1000):
    i_list = [int(j) for j in str(i)]
    i_list.sort(reverse=True)
    n1 = int(str(i_list[0]) + str(i_list[1]))
    if i_list[-1] == 0:
        if i_list[-2] == 0:
            n2 = int(str(i_list[-3]) + str(i_list[-1]))
        else:
            n2 = int(str(i_list[-2]) + str(i_list[-1]))
    else:
        n2 = int(str(i_list[-1]) + str(i_list[-2]))
    if n1 - n2 == 50:
        total_list.append(i)
print(total_list[-1])
