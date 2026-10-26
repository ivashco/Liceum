line = input()
while line != "":
    if "bug" in line or "BUG" in line:
        print(line)
        break
    elif (
        ("b" in line or "B" in line) and
        ("u" in line or "U" in line) and
        ("g" in line or "G" in line)
    ):
        print("BUG")
    else:
        print()
    line = input()
