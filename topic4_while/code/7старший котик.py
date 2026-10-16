name = input()
age = int(input())
name_old = name
age_old = age
while age > 0:
    if age > age_old:
        age_old = age
        name_old = name
    name, age = input(), int(input())
print(name_old)
