#LCM of Two Numbers using GCD
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
x,y=a,b
while a is not b:
    if a>b:
        a-=b
    else:
        b-=a
lcm=int((x*y)/a)
print('GCD=',a)
print('LCM=',lcm)
