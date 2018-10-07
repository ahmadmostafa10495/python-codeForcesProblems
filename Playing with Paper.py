a,b=map (int,input().split(" "))
i=1
while a!=b:
    if a>b:
        a-=b
    elif b>a:
        b-=a
    i+=1
print (i)
        
