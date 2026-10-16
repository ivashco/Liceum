line = input()
line_max = max(line)
line_min = min(line)
d = len(line) // 2
print(line_max * d + line_min * d)