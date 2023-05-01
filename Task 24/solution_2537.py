with open("Files/2537", "r") as f:
    abc = f.readline().strip()
    count = 0
    for i in range(len(abc) - 1):
        if abc[i] == "(" and abc[i + 1] == ")":
            count += 1
print(count)
