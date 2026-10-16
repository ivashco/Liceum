a = int(input())
b = int(input())
mn = min(a, b)
mx = max(a, b)
while mn != mx:
    mx = mx - mn
    mn, mx = min(mx, mn), max(mx, mn)
print(mn)
