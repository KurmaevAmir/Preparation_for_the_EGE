print("x", "y", "z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(z or x) or y and not(x) and (z and y <= z):
                print(x, y, z)
