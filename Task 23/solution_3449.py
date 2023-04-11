massive = {1}
massive2 = set()
for i in range(8):
    for j in massive:
        if j < 1024:
            massive2.add(j + 1)
            massive2.add(j + 5)
            massive2.add(j * 3)
    massive = massive2.copy()
    massive2.clear()
print(massive)
k = 0
for number in massive:
    if 1000 <= number <= 1024:
        k += 1
print(k)
