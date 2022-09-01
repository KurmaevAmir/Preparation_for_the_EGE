mass = ["п", "я", "т", "ь", "д", "н", "е", "й"]
mass.sort()
count = 0
last_count = 0
for a in mass:
    for b in mass:
        for c in mass:
            for d in mass:
                count += 1
                word = a + b + c + d
                if "я" not in word and "е" not in word:
                    if word.count(a) <= 1 and word.count(b) <= 1 and word.count(c) <= 1 and word.count(d) <= 1:
                        last_count = count
print(last_count)
