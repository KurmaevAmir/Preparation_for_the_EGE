import re

pattern = r"123[0,2,4,6,8]*45[0-9]{1}67"
for i in range(12345067, 12388845967, 100):
    if re.fullmatch(pattern, str(i)):
        if i % 257 == 0:
            print(i, i // 257)
