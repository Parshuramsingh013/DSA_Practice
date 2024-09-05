n = 5

for i in range(0,n):
    for j in range(0,n-i):
        print("*",end=" ")
    for j in range(0,i*2):
        print(" ",end=" ")
    for j in range(0,n-i):
        print("*",end=" ")
    print(" ")

for k in range (0,n):
    for j in range(0,k+1):
        print("*",end=" ")
    for j in range((n-k-1)*2):
        print(" ",end=" ")
    for j in range(0,k+1):
        print("*",end=" ")
    print(" ")   
