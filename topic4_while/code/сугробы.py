w = int(input())
snow = input()
n_snow = 0
while snow != "":
    n_snow += len(snow)
    snow = input()
print(n_snow // w)
