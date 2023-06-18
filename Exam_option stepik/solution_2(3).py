example1 = []
example2 = []
example3 = []
print("x y z w f1 f2")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = 0
                f2 = 0
                if (x or (not(y))) <= (w == z):
                    f1 = 1
                if (x or (not(y))) == (z <= w):
                    f2 = 1
                if f1 == f2 == 0 and [x, y, z, w].count(0) > 2:
                    example1.append((x, y, z, w))
                elif f1 == 0 and [x, y, z, w].count(1) > 1:
                    example2.append((x, y, z, w))
                elif f2 == 0 and [x, y, z, w].count(0) > 2:
                    example3.append((x, y, z, w))
for value in example1:
    print(*value)
print()
for value in example2:
    print(*value)
print()
for value in example3:
    print(*value)
print()
# yzxw
