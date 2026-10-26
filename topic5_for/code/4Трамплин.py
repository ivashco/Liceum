n1 = int(input())
n2 = int(input())
for i in range(n1, n2, 2):
    print(i, end=" ")
for i in range(n2, n1 - 1, -1):
    print(i, end=" ")

