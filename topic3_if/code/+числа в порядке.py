    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    mod1 = n1 % 3
    mod2 = n2 % 3
    mod3 = n3 % 3
    div1 = n1 // 3
    div2 = n2 // 3
    div3 = n3 // 3
    best, best_mod, best_div = n1, mod1, div1
    if mod2 > best_mod or (mod2 == best_mod and div2 > best_div):
        best, best_mod, best_div = n2, mod2, div2
    if mod3 > best_mod or (mod3 == best_mod and div3 > best_div):
        best, best_mod, best_div = n3, mod3, div3
    print(f"{best}\t{best_mod}\t{best_div}")


