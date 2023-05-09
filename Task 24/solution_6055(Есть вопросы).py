# with open("Files/6055", "r") as f:
#     abc = f.readline().strip()
#     total_list = []
#     for i in range(len(abc)):
#         if abc[i] == "F":
#             count_e = 0
#             count = 2
#             cond = False
#             for j in range(i + 1, len(abc)):
#                 if abc[j] == "E" and cond is False:
#                     count_e += 1
#                     cond = True
#                 elif abc[j] == "A" and cond:
#                     cond = False
#                 elif (abc[j] == "E" and cond) or (abc[j] == "A" and cond is False):
#                     break
#                 elif abc[j] == "F" and count_e >= 5 and cond:
#                     total_list.append(count)
#                     break
#                 count += 1
# print(max(total_list))

with open("Files/6055", "r") as f:
    abc = f.readline().strip()
    total_list = []
    for s in abc.split("F"):
        if s.count("E") >= 5:
            cond = False
            a = s.split("E")
            for n in range(1, len(a) - 1):
                if a[n].count("A") != 1:
                    cond = True
                    break
            if cond is False:
                total_list.append(len(s) + 2)
print(max(total_list))
# BCEBCAEAEAE
