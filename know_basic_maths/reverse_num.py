n = 5689

reverse_num =  0
while(n>0):
    last_digit = n%10
    # print(last_digit)
    reverse_num = reverse_num*10 + last_digit
    n = n//10

print(reverse_num)