from turtle import *

n = 6
x, y = 0, 0
left(90)
for i in range(20):
    x += 10
    y += 20
    goto(x * n, y * n)
    x += 5
    y += -15
    goto(x * n, y * n)
    x += -12
    y += -9
    goto(x * n, y * n)
print(x, y)
# 100
done()
