h = int(input())
max_h = 0
while int(h) >= 10:
    if h % 2 == 0 and h > max_h:
        max_h = h
    h = int(input())
print(max_h)
