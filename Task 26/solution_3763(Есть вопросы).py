with open("Files/3763", "r") as f:
    n = int(f.readline().strip())
    mass = []
    for i in range(n):
        mass.append(int(f.readline().strip()))
    mass.sort()
    average_value = sum(mass) // len(mass)
    k_list = []
    for number in mass:
        
print(len(k_list), max(k_list))
