with open("Files/3439", "r") as f:
    abc = f.readline().strip()
    count = 0
    for i in range(len(abc) // 2):
        if abc[i] == abc[len(abc) - 1 - i]:
            count += 1
print(count)
