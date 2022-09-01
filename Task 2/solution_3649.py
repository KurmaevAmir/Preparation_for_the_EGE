print("a", "b", "c", "d")
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if not(bool(b <= a)) and (c <= d) != (a and b and c and not(bool(d))):
                    print(a, b, c, d)
