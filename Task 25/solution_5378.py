import re

pattern = r"12[\d]*4[0-9]{1}65"
for i in range(124065, 10 ** 8 + 1):
    if re.fullmatch(pattern, str(i)):
        if i % 161 == 0:
            print(i, i // 161)
