line = input()
base = int(input())
i = len(line) - 1
dec = 0
for n in line:
    if int(n) >= base:
        print("Объект не подлежит телепортации.")
        break
    else:
        dec += int(n) * base ** i
    i -= 1
if  "0" in str(dec):
    print(dec)
    print("Возможно, в следующий раз получится лучше.")
else:
    print(dec)
    print("Поздравляем с успешной телепортацией!")

