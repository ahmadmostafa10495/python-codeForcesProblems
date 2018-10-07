a,b,c=map(int,input().split(' '))
if c>0:
    if a==b:
        print('YES')
    elif a>b:
        print ('NO')
    else:
        while 1:
            a+=c
            if b==a:
                print('YES')
                break
            elif a>b:
                print ('NO')
                break
elif c<0:
    if a==b:
        print('YES')
    elif a<b:
        print ('NO')
    else:
        while 1:
            a+=c
            if b==a:
                print('YES')
                break
            elif a<b:
                print ('NO')
                break
elif c==0:
    if a==b:
        print('YES')
    else :
        print ('NO')
    
