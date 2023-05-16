import math
import re

pattern = r"1[0-9]{1}2[\d]*0[\d]*2[0-9]{1}1"
for i in range(1020201, 1929990291, 10):
    if re.fullmatch(pattern, str(i)):
        definitive_list = []
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                definitive_list.append(j)
                if i // j != j:
                    definitive_list.append(i // j)
        if len(definitive_list) == 3:
            definitive_list.sort()
            print(i, definitive_list[1])
