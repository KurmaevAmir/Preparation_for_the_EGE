l = [(1, 1)]
r = []
k = 0
for i in range(100):
    for j in range(len(l)):
        if l[j][0] + l[j][1] + l[j][1] == 88:
            k += 1
        elif l[j][0] + l[j][1] + l[j][1] < 88:
            r.append((l[j][0] + l[j][1], l[j][1]))
        if l[j][0] + l[j][0] + l[j][1] == 88:
            k += 1
        elif l[j][0] + l[j][0] + l[j][1] < 88:
            r.append((l[j][0], l[j][0] + l[j][1]))
    l = r.copy()
    r.clear()
print(k)