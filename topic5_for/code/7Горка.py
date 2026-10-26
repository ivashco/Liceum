word = input()
i = 1
for char in word:
    print(*(char * i), sep="-", end="")
    i += 1
    if i == len(word) + 1:
        print(".")
    else:
        print(";")
