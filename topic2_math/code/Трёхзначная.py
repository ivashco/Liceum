line = int(input())
n_1 = line // 100
n_3 = line % 10
n_2 = line // 10 - n_1 * 10
n_max = max(n_1, n_2, n_3)
n_min = min(n_1, n_2, n_3)
n_avg = n_1 + n_2 + n_3 - n_max - n_min
print(str(n_avg) + str(n_max) + str(n_min))
