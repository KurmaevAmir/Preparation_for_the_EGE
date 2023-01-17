count = 0
for i in range(5, 10000000000, 10):
    if len((hex(i)[2::])) <= 8 and len((oct(i)[2:])) >= 11:
        count += 1
print(count)
