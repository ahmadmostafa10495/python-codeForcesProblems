c,n=map(int,input().split(" "))
st=input()
nd=input()
mylist=[]
o=n
while o>0:
    a = [str(x)  for x in input()]
    mylist.append(a)
    o-=1
i=0
j=0
while i<n:
    for x in mylist[i]:
        while j<c:
            if x==st[j]:
                x==nd[j]
            if x==nd[j]:
                x==st[j]
            j+=1
    print(mylist[i])
    i+=1
    
