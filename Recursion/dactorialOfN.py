 ## factorial Of N

n = int(input("enter the the number you want to print: "))

def sumNum(n):
    if n == 0:
        return 1
    return n * sumNum(n-1)

print(sumNum(n))