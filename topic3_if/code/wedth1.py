wedth = int(input())
heigth = int(input())
rib_1 = int(input())
rib_2 = int(input())
rib_3 = int(input())

if (
    (rib_1 <= wedth and rib_2 <= heigth and rib_2 <= wedth and rib_1 <= heigth)
    or (rib_3 <= wedth and rib_2 <= heigth and rib_2 <= wedth and rib_3 <= heigth)
    or (rib_1 <= wedth and rib_3 <= heigth and rib_3 <= wedth and rib_1 <= heigth)
):
    print("True")
else:
    print("False")
