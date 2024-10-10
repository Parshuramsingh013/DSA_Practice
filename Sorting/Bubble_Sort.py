## Bubble sort

n = int(input("Enter the number of elements : "))

arr = []

for i in range(n):
    elemet = int(input(f"enter the element {i+1}: "))
    arr.append(elemet)

print(arr)
for i in range(n-1,0,-1):
    for j in range(0,i):
        if(arr[j]>arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(f'sorted array using bubble sort : ',arr)


