n = 5

for i in range(0,n):
    # Print leading spaces
    for j in range(0,n-i-1):
        print(" ",end="")
    
    # Print the first half of the pattern
    for j in range(0,i+1):
        print(chr(65 + j),end="")
    
    # Print the second half of the pattern
    for j in range(i-1,-1,-1):
        print(chr(65 + j), end="")
    
    print()