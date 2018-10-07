x=int(input())
s=input()
i=0
r=x
a = [str (e) for e in s]
while i<x-1:
    if a[i]==a[i+1]:
        a.remove(a[i])
        x-=1
        i-=1
    i+=1
print(r-x)        
 
 
