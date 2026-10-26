n1 = int(input())
n2 = int(input())
start = int(input())
stop = int(input())
for i in range(start, stop + 1):
    if not (i % n1 == 0 or i % n2 == 0):
        print(i, end=' ')
print() 
# обратить внимание на not b и print(i, end=' ')