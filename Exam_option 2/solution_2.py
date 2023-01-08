print(f'c a d b')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if (((a and b) == (not(c))) and (b <= d)):
                    print(c, a, d, b)
print()
print(f'c a b d')
print(f'1 0 0 0')
print(f'1 0 1 0')
print(f'1 0 1 1')
print(f'1 1 0 0')
print(f'1 1 1 0')
