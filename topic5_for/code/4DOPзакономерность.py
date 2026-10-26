n1 = int(input())
n2 = int(input())
if n1 > n2:
    n2, n1 = n1, n2
for i in range(n1, n2):
    if i % 2 == 0:
        print(bin(i), end="")
        if i % 8 == 0:
            print("\t", end="")
            print(oct(i), end="")
            if i % 16 == 0:
                print("\t", end="")
                print(hex(i), end="")

        print()
