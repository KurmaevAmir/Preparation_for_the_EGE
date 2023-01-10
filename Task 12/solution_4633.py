total_list = []
count = 0
for i in range(3, 25):
    number = i * "8"
    while "555" in number or "888" in number:
        number = number.replace("555", "8", 1)
        number = number.replace("888", "55", 1)
    if number not in total_list:
        total_list.append(number)
        count += 1
    print(number)
print(len(total_list))
