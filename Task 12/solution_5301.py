total_list = []
count = 0
for i in range(1, 100):
    number = i * "1"
    while "1111" in number or "222" in number or "33" in number:
        if "1111" in number:
            number = number.replace("1111", "333", 1)
        elif "222" in number:
            number = number.replace("222", "11", 1)
        else:
            number = number.replace("33", "2", 1)
    if number not in total_list:
        total_list.append(number)
        count += 1
        print(number)
print(count)
