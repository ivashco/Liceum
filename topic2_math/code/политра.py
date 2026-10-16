from math import log2, ceil

m = int(input())
n = int(input())
color = int(input())
bit_color = ceil(log2(color))
byte_picture = ceil(bit_color * m * n / 8)
k = int(input())
print(ceil(byte_picture * k / 1024))
