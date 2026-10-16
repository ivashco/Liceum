phrase = input()
short = ''
while "end" not in phrase:
    if len(short) >= len(phrase) :
        short = phrase
    phrase = input()
print(short)
