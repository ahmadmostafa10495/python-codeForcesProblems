x=int(input())
i=0
a=[]
while i<x:
    a.append(input())
    i+=1
i=0
while i<x:
    if len(a[i])>10:
        print (a[i][0],end="")
        print(len(a[i])-2,end="")
        print(a[i][len(a[i])-1])
    else:
        print(a[i])
    i+=1
