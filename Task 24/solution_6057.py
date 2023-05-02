with open("Files/6057", "r") as f:
    s = f.readline().strip()
    max_len = -float("inf")
    number = 0
    while s != "":
        count = 1
        m = 0
        a = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
            else:
                if count > m:
                    m = count
                    a = s[i]
        if count > m:
            m = count
            a = s[i]
        if m > max_len:
            max_len = m
            number = s.count(a)
        elif m == max_len:
            if s.count(a) < number:
                number = s.count(a)
        s = f.readline().strip()
print(number)
