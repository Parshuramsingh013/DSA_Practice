## remove Duplication from sorted array



arr = [1,1,2,2,2,3,3]

i = 0
for j in range(1,len(arr)):
    if arr[i] != arr[j]:
        arr[i+1] = arr[j]
        i +=1
        
print(i+1)
