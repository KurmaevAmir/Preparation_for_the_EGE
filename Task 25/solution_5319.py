start = 700000
count = 0
while count != 5:
    if start % 13 == 0:
        if str(start)[-1] != "2" and str(start)[-4] != "4":
            if "0" in str(start) and "3" in str(start):
                if str(start).count("0") > 1 or str(start).count("3") > 1:
                    three_list = []
                    one_list = []
                    cond = True
                    interior_count = 0
                    for i in str(start):
                        if cond is False:
                            break
                        if i == "3":
                            three_list.append(interior_count)
                            for t in three_list:
                                if cond is False:
                                    break
                                for v in one_list:
                                    if t - v == 3:
                                        cond = False
                                        break
                        elif i == "0":
                            one_list.append(interior_count)
                        interior_count += 1
                    if cond is False:
                        start += 1
                        continue
                else:
                    if str(start).find("3") - str(start).find("0") == 3:
                        continue
            if "1" not in str(start)[0:-1]:
                print(start, sum([int(i) for i in str(start)]))
                count += 1
    start += 1

