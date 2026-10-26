a = int(input())
b = int(input())
max_n = max(a, b)
min_n = min(a, b)
while min_n != max_n:
    res = max_n - min_n
    min_n, max_n = min(min_n, res), max(max_n, res)
print(min_n)