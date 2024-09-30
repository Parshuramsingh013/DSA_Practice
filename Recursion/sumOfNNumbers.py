    ## Sum of n Numbers

n = int(input("enter the the number you want to print: "))

def sumofN(i,sum):
    if i < 0:
        print(sum)
        return
    sumofN(i-1,sum+i)

sumofN(n,0)