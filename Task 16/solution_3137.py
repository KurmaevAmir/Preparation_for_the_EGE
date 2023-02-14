def function(n):
    global sum_numbers
    sum_numbers += n * n
    if n > 1:
        sum_numbers += 2 * n + 1
        function(n - 2)
        function(n // 3)


for i in range(1000):
    sum_numbers = 0
    function(i)
    if sum_numbers > 3200000:
        print(i, sum_numbers)
        break
