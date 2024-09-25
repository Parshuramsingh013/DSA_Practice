n = 1223

original_n = n
reverse_num =  0
while(n>0):
    last_digit = n%10
    # print(last_digit)
    reverse_num = reverse_num*10 + last_digit
    n = n//10

if original_n == reverse_num:
    print("Pelindrome :", True)

else:
    print("Pelindrome :", False)
