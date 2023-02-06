def function(n):
    if n < 2:
        return 1
    elif n >= 2 and n % 3 == 0:
        return function(n / 3) + 1
    elif n >= 2 and n % 3 != 0:
        return function(n - 2) + 5


for i in range(10000):
    if function(i) == 73:
        print(i)
        break
