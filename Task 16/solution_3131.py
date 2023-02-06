count = 0


def function(n):
    global count
    count += 1
    if n >= 1:
        count += 1
        function(n - 1)
        function(n // 3)
        count += 1


function(280)
print(count)
