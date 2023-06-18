with open("Files/24(6).txt", "r") as f:
    input_string = f.readline().strip()
    vowels = ["A", "O"]
    for i in ["C", "D", "F"]:
        input_string = input_string.replace(i, "0")
    for i in ["A", "O"]:
        input_string = input_string.replace(i, "1")
    input_string = input_string.replace("011", "!").replace("001", "!")
    total = ""
    for symbol in input_string:
        if symbol != "!":
            total += "*"
        else:
            total += "!"
    total_list = [len(i) for i in total.split("*")]
print(max(total_list))
