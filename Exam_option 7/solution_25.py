from re import fullmatch

pattern = r'11[0-9]{2}4[\d]*56'
for i in range(1100456, 10 ** 8):
    if fullmatch(pattern, str(i)):
        if i % 211 == 0:
            print(i, i // 211)
