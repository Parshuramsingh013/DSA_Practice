arr = [1,2,4,5,6,8,9,52,3]


is_sorted = False
for i in range(1,len(arr)):
    if arr[i] >= arr [i-1]:
        is_sorted = True
    else:
        is_sorted = False
    
print(is_sorted)

