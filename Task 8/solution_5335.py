count = 0
for i in range(10000, 77777):
    if str(i).count("8") == 0 and str(i).count("9") == 0 and str(i).count("6") == 1:
        f = True
        for z in [1, 3, 5, 7]:
            if f'6{z}' in str(i) or f'{z}6' in str(i):
                f = False
                break
        if f:
            count += 1
print(count)
