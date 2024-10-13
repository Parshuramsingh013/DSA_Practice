arr = [5,10,6,2,3,9,8]

largest = arr[0]
for i in range(1,len(arr)):
    if arr[i]> largest:
        largest = arr[i]

print(largest)
