days = int(input())
t_max = -100
day = 0
for i in range(days):
    line = input()
    while line != "New day":
        t = float(line)
        if t_max < t:
            t_max = t
            day = i
        line = input()
print(t_max, day + 1)

