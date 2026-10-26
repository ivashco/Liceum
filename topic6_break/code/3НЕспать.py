line = input()
power = len(line)
idea = input()
while idea != "Можно спать.":
    if len(idea) % 3 == 0:
        power -= len(idea) // 3
    elif len(idea) % 2 == 0:
        power -= len(idea) // 2
    else:
        power -= 1
    if power <= 0:
        print(idea)
        break
    idea = input()
else:
    print(power)
    """_summary_else 
    """
