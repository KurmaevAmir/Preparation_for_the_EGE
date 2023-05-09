import re

with open("Files/5643", "r") as f:
    abc = f.readline().strip()
    pattern = r'12[0-9]{4}77[0-9]{2}9'
    for i in range(12999977999, 12000077009, -1):
        if re.fullmatch(pattern, str(i)):
            number = str(abs(i))
            if f'SS{i}SS' in abc:
                sum_number = 0
                multiplication_number = 1
                for j in range(len(number)):
                    if int(number[j]) % 2 != 0:
                        sum_number += int(number[j])
                    else:
                        multiplication_number *= int(number[j])
                print(sum_number + multiplication_number)
                break
