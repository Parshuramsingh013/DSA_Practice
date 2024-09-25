## Extract the Number


n = int(input("Enter the number : "))

while(n>0):
    last_digit = n%10
    print(last_digit)
    n = n//10

