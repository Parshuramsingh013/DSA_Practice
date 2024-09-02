"""
Printing for this pattern
        * * * *
        * * * 
        * * 
        * 
"""


n = 4

for i in range(0,n+1):
    for j in range(1,n-i+1):
        print("*",end=" ")
    print(" ")