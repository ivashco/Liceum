bus1, bus2 = int(input()), int(input())
bus1, bus2 = bus2, bus1
amount = 0
while (number := int(input())) != bus1 and number != bus2:
    amount += 1
print(amount)
