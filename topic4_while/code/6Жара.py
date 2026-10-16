max_t = int(input())
limit = max_t
while limit != 6000:
    max_t = max(limit, max_t)
    limit = int(input())
print(max_t)
