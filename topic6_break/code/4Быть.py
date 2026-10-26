vowel = "aeyuioAEYUIO"
line = input()
while line != '':
    for i in line:
        if i == " " or i not in vowel:
            print(i, end='  ')
    print()
    line = input()
