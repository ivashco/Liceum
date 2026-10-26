from math import ceil

start = int(input())
p = int(input())
if start < 0 or p < 0:
    print(-1)
elif start >= p:
    print(0)
else:
    print(ceil((p - start) / 780))
