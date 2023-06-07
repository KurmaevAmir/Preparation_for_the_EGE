import re

pattern = r'12\d*45\d*'
for i in range(1245, 129946):
    if re.fullmatch(pattern, str(i)):
        if i % 51 == 0:
            print(i, i // 51)
