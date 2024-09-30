## Print the Number From N to 1

n = int(input("enter the the number you want to print: "))

def printNum(i,n):
    if i < 1:
        return
    print(i)
    printNum(i-1,n)

printNum(n,n)