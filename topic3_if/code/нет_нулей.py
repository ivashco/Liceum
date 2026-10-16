"""_нет нулей_"""

line = input()
n = int(line)
if n % 2 == 0:
    print("Чётное! Это запрещено!")
elif len(line) < 6:
    print("Короткое! Это запрещено!")
elif n % 3 != 0 and n % 5 != 0:
    print("Не делится! Это запрещено!")
elif n % 11 == 0:
    print("Делится! Это запрещено!")
elif "0" in line:
    print(" Нули в числе! Это запрещено!")
else:
    print("Какое милое число!")
