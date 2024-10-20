arr = [1,1,2,2,3,3,4,4,6]


for i in range(len(arr)):
    n = arr[i]
    count =0
    for j in range(len(arr)):
        if n == arr[j]:
            count +=1

    if count == 1:
        print(n)