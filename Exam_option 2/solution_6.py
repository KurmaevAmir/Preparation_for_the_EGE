from turtle import left, forward, done, dot, goto, pu

n = 40
left(90)
for i in range(16):
    left(36)
    forward(4 * n)
    left(36)
pu()
for x in range(-8, 2):
    for y in range(-4, 4):
        goto(x * n, y * n)
        dot()
done() # 31
