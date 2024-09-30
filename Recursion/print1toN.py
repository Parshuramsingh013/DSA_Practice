## Print the Number From 1 to N

n = int(input("enter the the number you want to print: "))

def printNum(i,n):
    if i > n:
        return
    print(i)
    printNum(i+1,n)

printNum(1,n)