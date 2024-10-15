arr = [1,2,0,2,3,0,0,5,0,8]
n = len (arr)

temp = []
temp1 = []
for i in range(n):
    if (arr[i] != 0):
        temp.append(arr[i])
    else:
        temp1.append(arr[i])

temp.extend(temp1)
print(temp)


