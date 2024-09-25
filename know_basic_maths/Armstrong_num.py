n =153

original_num = n
sum = 0
while (n >0):
    last_digit = n %10
    sum = sum + last_digit**3
    n = n//10

print (sum)

if original_num == sum:
    print("Armstrong num :",True)

else:
    print("Armstrong num :", False)


