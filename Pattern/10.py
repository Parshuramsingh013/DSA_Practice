"""
Printing for this pattern

            *
            * * 
            * * * 
            * * * *
            * * *
            * *
            * 
"""

n = 4

for i in range(1,2*n):
    if i <= n:
        stars = i
    else:
        stars = 2 * n - i
    
    for j in range(stars):
        print("*", end="")
    print(" ")