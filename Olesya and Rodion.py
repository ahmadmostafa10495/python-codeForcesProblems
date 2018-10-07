n,t=map(int,input().split(' '))
i=10**n
i-=1
while 1:
    if i==0:
        print("-1")
        break
    if i%t==0:
        print(i)
        break
   
    i-=1    
