## Rotate the array to D place in left

arr = [1,2,3,6,4,8,9,7,4]


d = int(input("enter the number yu want rotate left : "))
d = d % len(arr)
temp = []
for i in range(d):
    temp.append(arr[i])

for i in range (d,len(arr)):
    arr[i-d] = arr[i]

for i in range(len(temp)):
    arr[len(arr)-d + i] = temp[i]

print(arr)