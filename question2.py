import math
n=input('type the numbers you wanted to get factorial:')
l=n.split(',')

for i in range(len(l)):
    l[i]=math.factorial(int(l[i]))

print(str(l)[1:-1])