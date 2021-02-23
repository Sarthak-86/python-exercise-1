d=input('please input numbers :')
l=d.split(',')
c=50
h=30
import math
for i in range(len(l)):
    a=2*c*int(l[i])/h
    l[i]=int(math.sqrt(a))

print(str(l)[1:-1])