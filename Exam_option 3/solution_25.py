from math import sqrt
import re


def main_1():
    count = 0
    pattern = r'[1,2,3,4,5,6,7,8,9]{1}6[\d]*6[\d]*[\d]{1}6'
    for mask in range(16606, 1000000):
        if re.fullmatch(pattern, str(mask)):
            definitive_list = []
            for i in range(1, int(sqrt(mask)) + 1):
                if mask % i == 0:
                    definitive_list.append(i)
                    if mask // i != i:
                        definitive_list.append(mask // i)
            if (6 in definitive_list) and (7 in definitive_list) and (8 in definitive_list):
                count += 1
                print(mask, sum(definitive_list))
                if count == 7:
                    return






def main():
    count = 0
    question_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    star_list = [""]
    for question in question_list[1:]:
        for star in star_list:
            cond = True
            if cond:
                for star2 in star_list:
                    cond2 = True
                    if cond2:
                        for question2 in question_list:
                            definitive_list = []
                            mask = int(f'{question}6{star}6{star2}{question2}6')
                            print(mask) # сразу переходит на шестизначное число после того,
                            # как поставил на первое место 1
                            if star2 != "":
                                if int(star2) % 10 == 0:
                                    cond = False
                                    cond2 = False
                                    break
                            elif len(star_list) == 1:
                                star_list.append("0")
                            else:
                                star_list.append(str(int(star_list[-1]) + 1))
                            for i in range(1, int(sqrt(mask)) + 1):
                                if mask % i == 0:
                                    definitive_list.append(i)
                                    if mask // i != i:
                                        definitive_list.append(mask // i)
                            if (6 in definitive_list) and (7 in definitive_list) and (8 in definitive_list):
                                count += 1
                                print(mask, sum(definitive_list))
                                if count == 7:
                                    return
                    else:
                        break
            else:
                break
main_1()
