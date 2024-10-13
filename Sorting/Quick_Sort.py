arr = [1,3,5,8,2,10,52,14]

def qs(arr, low, high):
    if (low< high):
        partion = quikSort(arr, low, high)
        qs (arr, low, partion - 1)
        qs(arr, partion+1, high)

def quikSort(arr, low, high):
    pivot= arr[low]
    i = low + 1
    j = high

    while (i < j):
        while( arr[i] <= pivot and i<= high):
            i += 1
        while(arr[j] > pivot and j >= low):
            j -= 1

        if (i<=j):
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j
        
def QS(arr):
    qs(arr,0,len(arr)-1)

QS(arr)
print(arr)