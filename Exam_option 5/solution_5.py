count = 0
for i in range(13 , 10000):
    i_bin = bin(i)[2:]
    if i % 2 == 0:
        i_bin = "1" + i_bin + "11"
    else:
        i_bin = "11" + i_bin + "0"
    number = int(i_bin, 2)
    if 500 <= number <= 1000:
        count += 1
print(count)
