t = int(input())
max_t = t
while t < 6000:
    max_t = max(t, max_t)
    t = int(input())
print(max_t)
