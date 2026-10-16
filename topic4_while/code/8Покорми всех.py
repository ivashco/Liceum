n = int(input())
n_min = n
while n >= 0:
    if n < n_min:
        n_min = n
    n = int(input())
print(n_min)
