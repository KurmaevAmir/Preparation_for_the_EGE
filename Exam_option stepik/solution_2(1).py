print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((not(x)) and (not(y))) or (y == z) or w):
                    print(x, y, z, w)
# zwyx
