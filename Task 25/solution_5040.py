import re

pattern = r"3[0-9]{1}458[\d]*3"
for i in range(304583, 394589994, 10):
    if re.fullmatch(pattern, str(i)):
        remainder_list = []
        number = i
        while number // 9 > 0:
            remainder_list.append(number % 9)
            number //= 9
        remainder_list.append(number)
        remainder_list = remainder_list[::-1]
        cond = True
        for j in range(len(remainder_list) - 1):
            if ord(str(remainder_list[j])) < ord(str(remainder_list[j + 1])):
                cond = False
                break
        if cond:
            print(i, sum(remainder_list))
