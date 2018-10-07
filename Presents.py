x=int(input())
e=[int (i) for i in input().split()]
z=0
r=[]
while z<x:
    r.append(0)
    z+=1
q=0
u=0
while q<x:
    while u<x:
        if e[u]==q+1:
            r[q]=u+1
            break
        u+=1
    u=0
    q+=1


l=0
while l<x:
    if l==(x-1):
        print(r[l])
        break
    print(r[l],end=" ")
    l+=1








  
