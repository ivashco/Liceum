from math import ceil, floor


N = int(input())
simbol = 33 * 2 + 27 * 2 + 2
bit_one = 1
while 2 ** bit_one < simbol:
    bit_one += 1
byte_one_mbr = ceil(bit_one * 100 / 8)
bit_res = 1
while 2 ** bit_res < N:
    bit_res += 1
byte_res = ceil(bit_res / 8)
print(byte_res)
byte_one_mbr = byte_res + byte_one_mbr
mbr = floor(N * 1024 / byte_one_mbr)
print(mbr)
