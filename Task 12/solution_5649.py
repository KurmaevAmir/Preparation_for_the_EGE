for k in range(100, 201):
    for m in range(100, 201):
        for n in range(100, 201):
            number = ">" + "1" * k + "2" * m + "*" * n
            while ">1" in number or ">2" in number or ">*" in number:
                number = number.replace(">1", "111>", 1)
                number = number.replace(">2", "1>", 1)
                number = number.replace(">*", "%2*>")
            if sum([int(i) for i in number if i != "%" and i != "*" and i != ">"]) == 1190:
                print(n)
                break
