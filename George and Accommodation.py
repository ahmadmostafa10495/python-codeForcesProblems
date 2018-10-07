n=int(input())
b=0
p=[]
q=[]
f=0
while b<n:
    z,m=map(int, input().split())
    p.append(z)
    q.append(m)
    if q[b]-p[b]>1:
        f+=1
    b+=1    
    
print(f)        
