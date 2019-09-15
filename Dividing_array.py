n=int(input())
array_a=list()
for i in range(n):
    array_a.append(int(input()))
half=int(n/2)
ch=0
array_b=list()
array_a.sort()
for i in range(half):
    if i==0:
        array_b.append(array_a[i])
        array_a.remove(array_a[i])
    else:
        for j in array_a:
            if j>array_b[-1]:
               array_b.append(j)
               array_a.remove(j)
               break
if len(array_b)!=half:
    ch=half-len(array_b) 
    for i in range(ch):
       x=array_b[-1]+1
       array_b.append(x)
for i in range(half):
    array_b.append(min(array_a))
    array_a.remove(array_b[-1])
print(ch)
print(array_b)
