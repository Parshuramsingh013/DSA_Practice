arr = [1,2,0,2,3,0,0,5,0,8]
n = len (arr)


j = -1

for i in range(n):
    if arr[i] == 0:
        j = i
        break
    
for i in range(j+1,n):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1

print(arr)

