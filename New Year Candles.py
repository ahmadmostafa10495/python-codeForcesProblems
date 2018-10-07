import math
a,b=map(int,input().split())
total=0
total+=a
e=a//b
f=(a%b)/b
while 1:
    if e>0:
        total+=(e)
        f+=(e%b)/b
        e=e//b
    else:
        break
g=f- math.floor(f)
f=int(f)
while 1:
    if f>0:
        total+=f
        g+=(f%b)/b
        f=f//b
    else:
        break
h=g-math.floor(g)
g=int(g)
while 1:
    if g>0:
        total+=g
        g=g//b
    else:
        break
print(total)    

