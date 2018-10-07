a=[]
for i in range (5):
    x=[int(i) for i in input()]
    a.append(x)
for q in range (5):
    if max(a[q])==1:
        r=q+1
        break
for m in range (5):
    if a[r-1][m]==1:
        c=m+1
        break
d=0    
if r==5 or r==1:
    d+=2
elif r==4 or r==2:
    d+=1
if c==5 or c==1:
    d+=2
elif c==4 or c==2:
    d+=1    



print (d)    
