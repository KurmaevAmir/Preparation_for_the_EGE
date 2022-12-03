from turtle import *

n = 10
x, y = 0, 0
left(90)
for i in range(2):
    x += 3
    y += 4
    goto(x * n, y * n)
    x += -3
    y += 4
    goto(x * n, y * n)
    x += -3
    y += -4
    goto(x * n, y * n)
    x += 3
    y += -4
    goto(x * n, y * n)
done()
# 20
