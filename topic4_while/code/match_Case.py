health = 100
run_away = False
while health > 0 and not run_away: # Пока есть здоровье и не убежали. 
    print("Bau ход (атака/защита/бег):")
    match input(): # Нам даже не надо хранить ввод — сразу выбираем. 
        case "атака":
            print("Атакую врага!")
            health -= 10 # Тратим силы.
        case "защита":
            print("(Защищаюсь!") 
            health+= 5 # Восстанавливаемся.
        case "бег":
            print("Бегу с поля боя!")
            run_away = True
        case _:
            print("Неизвестная команда.")
    print(f" Здоровье: {health}")
if health <= 0:
    print(" Игра окончена.")
else:
    print("Победа!")
