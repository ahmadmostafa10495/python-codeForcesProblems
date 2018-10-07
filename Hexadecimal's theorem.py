x=int(input())
f0=0
f1=1
f2=1
f3=2
f4=3
while 1:
    f0=f1
    f1=f2
    f2=f3
    f3=f4
    f4=f2+f3
    if x==0:
        print('0 0 0')
        break
    elif x==1:
        print ('1 0 0')
        break
    elif x==2:
        print ('1 1 0')
        break
    elif x==3:
        print ('1 1 1')
        break
    elif f4==x:
        print(f0,f1,f3)
        break
    
