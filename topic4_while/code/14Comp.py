prev = None
count = 0
while count < 3:
    n = int(input())
    if prev is None:
        prev = n
        count = 1
        print("Работает хорошо.")
    elif n == prev:
        count += 1
    else:
        prev = n
        count = 1
    if count < 3:
        print("Работает хорошо.")
print("Перезагрузка.")
