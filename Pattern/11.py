"""
Printing for this pattern

        1
        0 1
        1 0 1
        0 1 0 1
        1 0 1 0 1
"""


n = 3

for i in range(0,n):
    if i%2 == 0:
        start = 1
    else:
        start = 0

    for j in range(0,i+1):
        print(start,end=" ")
        start = 1 - start
    print(" ")
    
