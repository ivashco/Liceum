res1 = int(input())
res2 = 0
time = int(input())
while time > 0:
    if time <= res1:
        res2 = res1
        res1 = time
    elif res2 >= time > res1:
        res2 = time
    elif res2 == 0:
        res2 = time
    time = int(input())
print(res2)
