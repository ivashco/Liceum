energy = int(input())
step = 0
while energy > 0:
    step += 1
    value = int(input())
    if value > 0:
        energy -= 1
    else:
        if energy > abs(value):
            energy += 1
        else:
            energy -= 3
    print(step, energy)
