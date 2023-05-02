with open("Files/4139", "r") as f:
    abc = f.readline().strip()
    count = 3
    total_list = []
    pos_xyz = 1
    for i in range(4, len(abc)):
        try:
            if pos_xyz + 3 == abc.index("XYZ", i) == i:
                pos_xyz = abc.index("XYZ", i)
                count += 3
                permissible_count = 0
            elif abc.index("XYZ", i) == i:
                count = 3
                pos_xyz = abc.index("XYZ", i)
                permissible_count = 0
            elif permissible_count < 2:
                permissible_count += 1
            elif permissible_count == 2:
                total_list.append(count)
                count = 0
                permissible_count = 3
        except:
            break
print(max(total_list))
