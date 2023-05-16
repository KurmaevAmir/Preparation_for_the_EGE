import re

pattern = r"4[\d]*1[0-9]{1}009"
for i in range(2000, 10 ** 5 + 1):
    if re.fullmatch(pattern, str(i ** 2)):
        print(i, i ** 2)
