with open("Files/24(5).txt", "r") as f:
    input_string = f.readline().strip()
    input_string = input_string.replace("XZZY", "!")
    input_string = input_string.split("!")
    print(max([len(i) for i in input_string]) + 6)
