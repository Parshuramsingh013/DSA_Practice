## Insertion sort

n = int(input("Enter the number of element of the array : "))

arr = []

for i in range(n):
    element = int(input(f'enter the element{i+1} :'))
    arr.append(element)

# print(arr)

for i in range(0,n):
    j = i
    while(j>0 and arr[j-1] > arr[j]):
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j -= 1

print("This is the array is sorted by Insertion sort :", arr)