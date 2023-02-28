function_list = [0] * 2024
function_list[1] = 1
for i in range(2, 2024):
    function_list[i] = i * function_list[i - 1]
print(function_list[2023] // function_list[2020])
