import re

pattern = r'12[0-9]{2}1[\d]*56'
for i in range(1200156, 12991957):
    if re.fullmatch(pattern, str(i)):
        if i % 317 == 0:
            print(i, i // 317)
