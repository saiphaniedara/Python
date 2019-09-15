class Stack:
    def __init__(self):
        self.stacka=list()
        self.tracestack=list()
    def pushs(self,x):
        self.stacka.append(x)
    def pops(self):
        self.tracestack.pop()
s=Stack()
n=int(input())
k=int(input())
for i in range(n):
    s.pushs(int(input()))
s.stacka.reverse()
s.tracestack=s.stacka.copy()
maxtop=s.stacka[-1]
elepop=list()
ite=int(k/2)+1
for i in range(ite):
    pop=ite-i
    for x in range(pop):
      elepop.append(s.tracestack[-1])
      s.pops()
    elepop.clear()
    if(s.tracestack[-1]>maxtop):
        maxtop=s.tracestack[-1]
    s.tracestack=s.stacka.copy()
print(maxtop)

