from turtle import *

c = 30
x = 0
y = 0
for i in range(3):
    x += 3 # 3
    y += 2 # 2
    goto(x * c, y * c)
    x += -2 # 1
    y += 3 # 5
    goto(x * c, y * c)
    x += -3 # -2
    y += -2 # 3
    goto(x * c, y * c)
    x += 2 # 0
    y += -3 # 0
    goto(x * c, y * c)
done()
