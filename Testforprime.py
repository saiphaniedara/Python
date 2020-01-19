#Check whether the given integer is Prime Number or not
import math
a=int(input('Enter a number: '))
b=int(math.sqrt(a))
if a==1:
    print('Neither prime nor composite')
for i in range(2,b+1):
    if a%i==0:
        print('Not a prime')
        break
    elif i==b:
        print('Is a prime')
