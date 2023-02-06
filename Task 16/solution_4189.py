def function(n):
    if n == 0:
        return 2
    elif 0 < n <= 15:
        return function(n - 1)
    elif 15 < n < 95:
        return 1.6 * function(n - 3)
    elif n >= 95:
        return 3.3 * function(n - 2)


number = str(int(function(33)))
max_count = -float('inf')
max_number = -float('inf')
for symbol in range(10):
    if max(max_count, number.count(str(symbol))) != max_count:
        max_number = symbol
        max_count = number.count(str(symbol))
print(max_number)
