    days = int(input())
    start = int(input())
    day = 1
    while day <= days:
        if start > 1:
            for k in range(start - 1):
                print("", end="\t")
            for i in range(start - 1, 7):
                if i == 6:
                    print(day)
                else:
                    print(day, end="\t")
                day += 1
        for i in range(7):
            if i == 6:
                print(day)
            else:
                print(day, end="\t")
            day += 1
            if day > days:
                break
        start = 1
    print()
