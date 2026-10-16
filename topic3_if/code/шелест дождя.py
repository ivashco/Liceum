rain = input()
if (
    ('Ш' in rain or 'СТ' in rain or 'ш' in rain or 'ст' in rain)
    and 'р' not in rain and 'Р' not in rain
    ):
    print('Мечта!')
elif (
      ('Ш' in rain or 'СТ' in rain or 'ш' in rain or 'ст' in rain)
      and ('р' in rain or 'Р' in rain)
    ):
    print('Грянет буря!')
else:
    print('А где же дождь?'
