#GCD of Two Numbers
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
while a is not b:
    if a>b:
        a=a-b
    else:
        b=b-a
print('GCD=',a)
