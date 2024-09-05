n = 3  # This is the middle number (size of the pattern)

size = 2 * n - 1  # The total size of the pattern

for i in range(size):
    for j in range(size):
        # Determine the minimum distance to the edges
        min_dist = min(i, j, size - i - 1, size - j - 1)
        # The value to print is determined by how close the position is to the edge
        print(n - min_dist, end=" ")
    print()