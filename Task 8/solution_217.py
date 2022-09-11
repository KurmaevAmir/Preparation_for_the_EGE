symbols = ["К", "Л", "Р", "Т"]
symbols.sort()
symbols_list = []
for i in symbols:
    for j in symbols:
        for x in symbols:
            for y in symbols:
                symbols_list.append(i + j + x + y)
print(symbols_list[66])
