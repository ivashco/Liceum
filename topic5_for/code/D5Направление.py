start = int(input())
stop = int(input())
step = int(input())
dop = 1
if start > stop:
    step = -step
    dop = -dop
for i in range(start, stop + dop, step):
    print(i)
