test=int(input())
tests=test
mylist=[]
while tests>0:
    tests-=1
    x=int (input())
    while 1:
        x+=1
        r=str(x)
        if len(r)==2:
            if r[0]==r[1]:
                mylist.append (x)
                break
        elif len(r)==3:
            if r[0]==r[2]:
                mylist.append (x)
                break
        elif len(r)==4:
            if r[0]==r[3] and r[1]==r[2]:
                mylist.append(x)
                break
        elif len (r)==5:
            if r[0]==r[4] and r[1]==r[3]:
                mylist.append (x)
                break
test-=1
i=0
while 1:
    print (mylist[i])
    if test==i:
        break
   
    i+=1
    
