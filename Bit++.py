m=x=int(input())
a=[]
while m>0:
    m-=1
    a.append(input())
i=0
e=0
while e<len(a):
    if a[e]=='X++' or a[e]=='++X':
        i+=1
    elif a[e]=='X--' or a[e]=='--X':
        i-=1
    e+=1    
print (i)
