prev = int(input())
current = int(input())
counter = 0
while current != 0:
    next = int(input())
    if prev < current > next and next != 0:
        counter += 1
    prev = current
    current = next
print(counter)
