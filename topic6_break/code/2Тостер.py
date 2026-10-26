total_level = int(input())
time = int(input())
level = 0
for i in range(time):
    power = int(input())
    level += power
    if level >= total_level:
        print(f"Ваш хлеб уже готов! Степень поджаривания {level}.")
        break
else:
    print(f"Хлеб поджарен до степени {level}.")
    """внимание на break  и блок else  в цикле for
    """