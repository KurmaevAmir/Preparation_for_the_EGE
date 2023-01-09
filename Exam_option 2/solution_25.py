import math


def main():
    que = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    star = [""]
    count = 0
    for x in star:
        cond_y = True
        for y in star:
            if cond_y is False:
                break
            for z in que:
                mask = int(f'6{x}97{y}5{z}')
                if y != "":
                    if int(y) % 10 == 0:
                        cond_y = False
                        break
                elif len(star) == 1:
                    star.append("0")
                else:
                    star.append(str(int(star[-1]) + 1))
                count_divisors = 0
                cond = False
                divisors_list = []
                for i in range(1, int(math.sqrt(mask)) + 1):
                    if mask % i == 0:
                        if i % 2 == 0:
                            count_divisors += 1
                            divisors_list.append(i)
                        if mask // i != i:
                            if (mask // i) % 2 == 0:
                                count_divisors += 1
                                divisors_list.append(mask // i)
                if count_divisors > 3:
                    print(mask, sum(divisors_list))
                    count += 1
                    if count == 7:
                        return


main()
