s=int(input())
a=[]
b=[]
t=0
while t<s:
    g,n=map(int,input().split())
    a.append(g)
    b.append(n)
    t+=1
N=0
t=0
p=0
while t<s:
    N-=a[t]
    N+=b[t]
    if N>p:
        p=N
    t+=1
print (p)
