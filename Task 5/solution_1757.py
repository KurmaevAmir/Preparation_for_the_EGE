for i in range(256):
    i_bin = int(bin(i)[2:])
    number_bin = 11111111 - i_bin
    number = int(str(number_bin), 2)
    if number - i == 99:
        print(i)
        break
        
