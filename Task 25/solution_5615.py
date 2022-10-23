import math
prime_numbers = [2, 3, 5, 7]
for n in range(11, 10 ** 5 + 10, 2):
    if n % 10 != 5:
        for i in prime_numbers:
            if i > (int(math.sqrt(n)) + 1):
                prime_numbers.append(n)
                break
            if n % i == 0:
                break
        else:
            prime_numbers.append(n)
prime_numbers.sort()
x = '101'
y = 0
number = f'9{x}{y}'
count = 0
while int(number) <= 10 ** 7:
    for y in range(10):
        number = f'9{"0" + x}{y}'
        if int(number) % 9998 == 0:
            if int(number) > 10 ** 7:
                break
            print(number, int(number) // 9998)
    for y in range(10):
        number = f'9{x}{y}'
        if int(number) % 9998 == 0:
            print(number, int(number) // 9998)
    x = str(prime_numbers[count])
    count += 1
    number = f'9{x}{y}'
