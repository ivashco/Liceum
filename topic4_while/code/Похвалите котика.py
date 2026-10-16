praise = input()
len_praises = 0
number = 0
while "Scat" not in praise and "scat" not in praise:
    len_praises += len(praise)
    number += 1
    praise = input()
print(round(len_praises / number, 5))
