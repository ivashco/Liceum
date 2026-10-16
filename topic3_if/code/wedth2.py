wedth = int(input())
heigth = int(input())
rib_1 = int(input())
rib_2 = int(input())
rib_3 = int(input())

rib_min = min(rib_1, rib_2, rib_3)
rib_max = max(rib_1, rib_2, rib_3)
rib_avg = rib_1 + rib_2 + rib_3 - rib_min - rib_max
if min(wedth, heigth) >= rib_min and max(wedth, heigth) >= rib_avg:
    print(True)
else:
    print(False)

