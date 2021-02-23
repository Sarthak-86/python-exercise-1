n=input('please enter numbers : ')
l=n.split(',')
r=[]
for i in range(int(l[0])):
    d=[]
    for j in range(int(l[1])):
        d.append(i*j)
    r.append(d)

print(r)