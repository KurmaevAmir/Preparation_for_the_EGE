function_list = [0] * 1000
function_list[0] = 0
total_list = []
for i in range(1, 1000):
    if i % 2 == 0:
        function_list[i] = function_list[i // 2] + 3
    else:
        function_list[i] = 2 * function_list[i - 1] + 1
    if function_list[i] not in total_list:
        total_list.append(function_list[i])
print(len(total_list))
