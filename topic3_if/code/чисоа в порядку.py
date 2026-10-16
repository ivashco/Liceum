n1 = int(input())
n2 = int(input())
n3 = int(input())
mod1 = n1 % 3
mod2 = n2 % 3
mod3 = n3 % 3
div1 = n1 // 3
div2 = n2 // 3
div3 = n3 // 3
if mod1 != mod2 and mod1!= mod3 and mod2 != mod3:
    if mod1 > mod2 > mod3:
        print(f"{n1}\t{mod1}\t{div1}")
    elif mod2 > mod3 > mod1:
        print(f"{n2}\t{mod2}\t{div2}")
    else:
        print(f"{n3}\t{mod3}\t{div3}")
elif mod1 == mod2 > mod3:
    if div1 > div2:
        print(f"{n1}\t{mod1}\t{div1}")
    else:
        print(f"{n2}\t{mod2}\t{div2}")
elif mod2 == mod3 > mod1:
    if div3 > div2:
        print(f"{n3}\t{mod3}\t{div3}")
    else:
        print(f"{n2}\t{mod2}\t{div2}")
elif mod3 == mod1 > mod2:
    if div3 > div2:
        print(f"{n3}\t{mod3}\t{div3}")
    else:
        print(f"{n1}\t{mod1}\t{div1}")
elif mod1 > mod2 >= mod3:
    print(f"{n1}\t{mod1}\t{div1}")
elif mod2 > mod3 >= mod1:
    print(f"{n2}\t{mod2}\t{div2}")
elif mod3 > mod1>= mod2:
    print(f"{n3}\t{mod3}\t{div3}")
elif mod1 == mod2 == mod3:
    if div1 > div2 and div1 > div3:
        print(f"{n1}\t{mod1}\t{div1}")
    elif div2 > div1 and div2 > div3:
        print(f"{n2}\t{mod2}\t{div2}")
    else:
        print(f"{n3}\t{mod3}\t{div3}")

