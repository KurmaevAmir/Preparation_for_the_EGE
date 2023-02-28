def function(n):
    if n <= 5:
        return n
    elif n % 4 == 0:
        return n + function(n // 2 - 1)
    else:
        return n + function(n + 2)


for i in range(500):
    try:
        answer_function = function(i)
    except:
        continue
    else:
        n = i
print(n)
