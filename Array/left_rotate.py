## Left rotation by one bit

arr = [1,2,3,4,5]
temp = arr[0]
n = len(arr)

for i in range(1,len(arr)):
    arr [i-1] = arr[i]

arr[n-1] = temp

print(arr)