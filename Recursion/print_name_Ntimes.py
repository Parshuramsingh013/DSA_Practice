## Prine the name N times


n = int(input("enter the the number you want to print the name : "))

def printname(i,n):
    if i > n:
        return
    print("ajit")
    printname(i+1,n)

printname(1,n)