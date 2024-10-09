n = int(input("Enter the number of elements : "))

arr = []

for i in range(n):
    elemet = int(input(f"enter the element {i+1}: "))
    arr.append(elemet)

for i in range(0,n-1):
    min = i
    for j in range(i+1,n):
        if (arr[j]<arr[min]):
            min = j
    arr[min], arr[i] = arr[i],arr[min]


print(f'sorted array : ',arr)
