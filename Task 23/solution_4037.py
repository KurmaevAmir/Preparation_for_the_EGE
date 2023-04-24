massive = {2}
massive2 = set()
for i in range(15):
    for j in massive:
        massive2.add(j + 2)
        massive2.add(j * 2 + 1)
    massive = massive2.copy()
    massive2.clear()
print(len(massive))
