function_list = [0] * 1000000000
function_list[0] = 5
for i in range(1, 1000000000):
    if i % 2 == 0:
        function_list[i] = 1 + function_list[i // 2]
    else:
        function_list[i] = function_list[i // 2]
print(function_list.count(7))
