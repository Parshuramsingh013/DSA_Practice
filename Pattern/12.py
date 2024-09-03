n= 4

for i in range(1, n + 1):
        # Print increasing part
        for j in range(1, i + 1):
            print(j, end=" ")
        
        # Add spaces between the parts
        print(" " * (2 * (n - i)), end=" ")
        
        # Print decreasing part
        for j in range(i, 0, -1):
            print(j, end=" ")
        
        print()
