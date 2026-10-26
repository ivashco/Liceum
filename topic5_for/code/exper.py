w1 = int(input())
w2 = int(input())
b1  = int(input())
b2 = int(input())
b3 = int(input())
max_w = max(w1, w2)
min_w = min(w1, w2)
max_b = max(b1, b2, b3)
min_b = min(b1, b2, b3)
avg_b = b1 + b2 + b3 - max_b - min_b
if min_b <= min_w and avg_b <= max_w:
    print(True)
else:
    print(False)
