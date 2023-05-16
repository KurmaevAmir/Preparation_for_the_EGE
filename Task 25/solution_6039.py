import re

pattern = r"1[0-9]{1}58[\d]*129"
for i in range(1058129, 10 ** 8 + 1):
    if re.fullmatch(pattern, str(i)):
        if i % 117 == 0 and i % 119 != 0 and i % 121 != 0:
            print(i, i // 117)
        elif i % 177 != 0 and i % 119 == 0 and i % 121 != 0:
            print(i, i // 119)
        elif i % 117 != 0 and i % 119 != 0 and i % 121 == 0:
            print(i, i // 121)
