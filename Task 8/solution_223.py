symbols = ["П", "О", "Р", "Т"]
symbols.sort()
position = []
count = 0
for i in symbols:
    for j in symbols:
        for x in symbols:
            for y in symbols:
                for z in symbols:
                    if i + j + x + y + z == "ТОПОР":
                        position.append(count)
                    elif i + j + x + y + z == "РОПОТ":
                        position.append(count)
                    count += 1
print(abs(position[0] - position[1]) + 1)
