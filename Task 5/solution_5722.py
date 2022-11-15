count = 0
for i in range(1000, 10000):
    i = str(i)
    if int(i[0]) % 4 == 0:
        i = i.replace(i[0], "9", 1)
    if int(i[0]) % 2 == 0 and int(i[0]) % 4 != 0:
        i = i.replace(i[0], "3", 1)
    if i[0] == "9" and oct(int(i))[-1] == "4":
        count += 1
print(count)
