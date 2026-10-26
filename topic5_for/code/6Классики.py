n1 = int(input())
n2 = int(input())
step = int(input())
for i in range(n1, n2 + 1, step):
    if i == n1:
        print(i, end='')
    else:
        print(",", i, end='')
print()

