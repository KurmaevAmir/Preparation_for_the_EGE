import math


def function(number):
    a = 2
    mass = []
    while a ** 2 <= number:
        if number % a == 0:
            mass.append(a)
            number //= a
        else:
            a += 1
    if number > 1:
        mass.append(number)
    return mass


def main():
    k = 1
    count = 0
    while count != 5:
        number = 500000000 + k
        total_massive = function(number)
        if len(total_massive) < 3:
            count += 1
            product = number // min(total_massive)
            print(k, product)
        k += 1


if __name__ == '__main__':
    main()
