lang = input()
n = int(input())
word = input()
if lang == "РУС":
    ltrst = 32
    start = ord("А")
elif lang == "ENG":
    ltrst = 26
    start = ord("A")
cipher = ""
for liter in word:
    new_letter = (ord(liter) - start + n) % ltrst + start
    print(chr(new_letter), end="")
print()
