from math import ceil


slot = int(input())
setup = int(input())

if slot >= 0 and setup >= 0:
    if slot <= setup:
        print(ceil((setup - slot)/780))
    else:
        print(0)
else:
    print(-1)
