    ## Sum of n Numbers functional way

n = int(input("enter the the number you want to print: "))

def sumNum(n):
    if n == 0:
        return 0
    return n + sumNum(n-1)

print(sumNum(n))