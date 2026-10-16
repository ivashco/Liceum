word = input()
omen = input()
good_omen = ''
while omen != '':
    if word in omen and (omen < good_omen and good_omen != ''):
        if omen < good_omen:
            good_omen = omen
    omen = input()
print(good_omen)
