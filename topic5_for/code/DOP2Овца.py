    n = int(input())
    for i in range(1, n + 1):
        ones = i % 10
        tens = i % 100
        if 11 <= tens <= 19:
            res = 'овец'
        elif ones == 1:
            res = 'овца'
        elif 2 <= ones <= 4:
            res = 'овцы'
        else:
            res = 'овец'
        print(i, res)
