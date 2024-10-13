arr = [5,6,9,9,8,1,3,7]

largest = arr[0]

for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]

secondLargest = -1
for i in range(len(arr)):
    if arr[i]> secondLargest and arr[i]!= largest:
        secondLargest = arr[i]

print(secondLargest)