x=input()
i=0
t=0
while i<len(x):
    if t==0:
        if x[i]=='h':
            t=1
    elif t==1:
        if x[i]=='e':
            t=2
    elif t==2:
        if x[i]=='l':
            t=3
    elif t==3:
        if x[i]=='l':
            t=4
    elif t==4:
        if x[i]=='o':
            t=5
    i+=1
if t==5:
    print('YES')
else:
    print('NO')
