with open("Files/24(2)", "r") as f:
    input_string = f.readline().strip()
    input_string = input_string.replace("E", "A")
    while "AAA" in input_string:
        input_string = input_string.replace("AAA", "AA AA")
    input_string = input_string.split()
    print(len(max(input_string, key=len)))
