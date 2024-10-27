arr = [5,6,9,9,8,1,3,7]

# First Way
largest = arr[0]

for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]

secondLargest = -1
for i in range(len(arr)):
    if arr[i]> secondLargest and arr[i]!= largest:
        secondLargest = arr[i]

print(secondLargest)

# Second way
largest = 1
secondLargets = -1

for i in range(len(arr)):
    if arr[i] > largest:
        secondLargets = largest
        largest = arr[i]
        
    elif arr[i] > secondLargets and arr[i] != largest:
        secondLargets = arr[i]

print(secondLargets)