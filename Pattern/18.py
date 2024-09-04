n = 5
    # TUF 
for i in range (0,n):
    for j in range(0,i+1):
        print(chr(64+n-i+j),end=" ")
    print(" ")


    # coding ninja 
for i in range (0,n):
    for j in range(0,i+1):
        print(chr(64+n-j),end=" ")
    print(" ")