    ## revers the array using recursion

array = [1,2,3,4,5,6,7,8,9]

def swapArr(l,r):
    if l >= r:
        return
    array[l], array[r] = array[r], array[l]
    swapArr(l+1,r-1)

swapArr(0,len(array)-1)
print(array)