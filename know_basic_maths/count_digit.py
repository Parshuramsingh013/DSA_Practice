## Count The Digit

## First way
n = 326
count = 0
while (n > 0):
    last_digit = n % 10
    count = count+1
    n = n // 10

print (count)

## Second Way

import math

N = 3256584

count = int(math.log10(N)+1)
print(count)