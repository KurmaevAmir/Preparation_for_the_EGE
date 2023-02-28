function_list = [0] * 10002
function_list[10000] = 10000
function_list[10001] = 10001
for i in range(9999, 0, -1):
    if i % 4 != 0 and i % 2 != 0: # Потому что они ссылаются на, те что делятся на 4
        function_list[i] = 1 + function_list[i + 2]
for i in range(4, 9997, 4):
    function_list[i] = i // 4 + function_list[i // 4 + 2]
    function_list[i - 2] = 1 + function_list[i]
print(function_list[174] - function_list[3])
