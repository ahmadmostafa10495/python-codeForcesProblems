x=int(input())
a=[int(i) for i in input().split()]
q=0
w=x-1
indexs=0
indexb=0
sm=min(a)
bi=max(a)
total=0
while q<x:
    if a[q]==bi:
        indexb=q
        break
    q+=1
while w>0: 
    if a[w]==sm:
        indexs=w
        break
    w-=1
    
if indexb>indexs:
    total-=1
total+=indexb
indexs=x-indexs-1
total+=indexs
print(total)
