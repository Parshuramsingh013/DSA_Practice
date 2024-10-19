arr = [1,1,0,1,1,1,0,1,1]

count = 0
max = 0 
n = len(arr)

for i in range(n):
    if arr[i] == 1:
        max += 1
        if max > count:
            count =  max
    else:
        max = 0

print(count)
    