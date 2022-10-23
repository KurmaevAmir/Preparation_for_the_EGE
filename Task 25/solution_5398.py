x = ""
count_x = 0
count_start = 0
intermediate_list = []
cond = True
digit = 10
count = 0
while count_start != 5:
    mask = f"12345{x}76"
    if int(mask) % 73 == 0:
        print(mask, int(mask) // 73)
        count_start += 1
    if x == "":
        x = 0
    elif cond:
        if len(intermediate_list) == digit:
            cond = False
            digit *= 10
            x = "0" + str(intermediate_list[0])
            count = 1
        else:
            intermediate_list.append(x)
            count_x += 1
            x = str(count_x)
    else:
        if count == len(intermediate_list):
            cond = True
            count_x += 1
            x = str(count_x)
            continue
        x = "0" + str(intermediate_list[count])
        count += 1
