"""
Printing for this pattern
           *
         * * *
       * * * * * 
       * * * * *
         * * * 
           *  
"""
n = 4

for i in range(0,n):

    # space
        for j in range(0,n-i-1):
            print(" ",end="")

    # star
        for k in range(0,2*i+1):
            print("*",end="")

        print(" ")
for i in range(0,n):

    # space
    for j in range(0,i):
        print(" ",end="")

    # star
    for k in range(0,2*n-(2*i+1)):
        print("*",end="")
    
    print(" ")