count = 0
for i in range(4000, 9000):
    if int(str(i)[0]) % 4 == 0:
        r = "9" + str(i)[1:]
        if oct(int(r))[-1] == "4":
            count += 1
print(count)
