for i in range(1, 1000):
    n1 = hex(i)[2:]
    n2 = oct(i)[2:]
    n3 = i
    remainder_list = []
    while n3 // 4 > 0:
        remainder_list.append(str(n3 % 4))
        n3 //= 4
    remainder_list.append(str(n3))
    n3 = "".join(remainder_list[::-1])
    n4 = bin(i)[2:]
    if n1[0] == "e" and n2[1] == "5" and n3[3] == "1" and n4[5] == "1":
        print(i)
        break
