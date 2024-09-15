n = 3 





size = 2 * n - 1 

for i in range(size):
    for j in range(size):
        min_dist = min(i, j, size - i - 1, size - j - 1)
        print(n - min_dist, end=" ")
    print()