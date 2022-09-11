symbols = ["А", "О", "У"]
symbols.sort()
count1 = 0
count2 = 0
count = 0
for i in symbols:
    for j in symbols:
        for x in symbols:
            for y in symbols:
                for z in symbols:
                    if i + j + x + y + z == "УАУАУ":
                        count1 = count
                    elif i + j + x + y + z == "ОУОУА":
                        count2 = count
                    count += 1
print(abs(count1 - count2) + 1)
