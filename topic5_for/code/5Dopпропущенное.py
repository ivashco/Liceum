n1 = int(input())
n2 = int(input())
step = int(input())
first = True
for k in range(n1, n2 + 1, -step):
    print(k - 1, end="")
    for i in range(k - 2, k - step, -1):
        if i > n2:
            print("+", end="")
            print(i, end="")
    print()
