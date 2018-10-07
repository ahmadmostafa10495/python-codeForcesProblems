n,k=map(int,input().split())
a=[int(i)  for i in input().split()]
while 1:
    if a[len(a)-1]==a[k-1]:
        break
    if len(a)>k:
        a.pop()
    else:
        break
c=len(a)-1    
while 1:
    if len(a)==0:
        break
    if a[c]==0:
        a.pop()
    else:
        break
    c-=1    
print (len(a))
