max_t = int(input())
limit = max_t

while (limit := int(input())) != 6000:
    max_t = max(limit, max_t)

print(max_t)
